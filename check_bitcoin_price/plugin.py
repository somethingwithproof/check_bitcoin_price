#!/usr/bin/env python3
"""
Nagios plugin to check Bitcoin price.

This plugin fetches the current Bitcoin price from a public API
and returns appropriate Nagios status codes based on configured thresholds.
"""

import argparse
import math
import sys
from typing import NamedTuple, Never

import requests

# Nagios exit codes
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

# Default API endpoint (CoinGecko - free, no API key required)
DEFAULT_API_URL = "https://api.coingecko.com/api/v3/simple/price"
DEFAULT_TIMEOUT = 10
DEFAULT_CURRENCY = "usd"


class ConfigurationError(ValueError):
    """Invalid monitoring check configuration."""


class PluginArgumentParser(argparse.ArgumentParser):
    """Report invalid arguments as UNKNOWN rather than CRITICAL (exit 2)."""

    def error(self, message: str) -> Never:
        raise ConfigurationError(message)


def validate_thresholds(low: float | None, high: float | None) -> None:
    """Require finite, nonnegative bounds in ascending order."""
    for value in (low, high):
        if value is not None and (not math.isfinite(value) or value < 0):
            raise ConfigurationError("Thresholds must be finite, nonnegative numbers")
    if low is not None and high is not None and low > high:
        raise ConfigurationError("Low threshold must not exceed high threshold")


def parse_price(price: object) -> float:
    """Normalize a price without allowing invalid data to report OK."""
    message = "Bitcoin price must be a finite, nonnegative number"
    if isinstance(price, bool) or not isinstance(price, (int, float, str)):
        raise ValueError(message)
    try:
        value = float(price)
    except (ValueError, OverflowError) as exc:
        raise ValueError(message) from exc
    if not math.isfinite(value) or value < 0:
        raise ValueError(message)
    return value


class ThresholdResult(NamedTuple):
    """Result of threshold check."""

    status: int
    message: str


class BitcoinPriceChecker:
    """Class to check Bitcoin price against thresholds."""

    def __init__(
        self,
        api_url: str = DEFAULT_API_URL,
        timeout: int = DEFAULT_TIMEOUT,
        currency: str = DEFAULT_CURRENCY,
    ):
        """
        Initialize the Bitcoin price checker.

        Args:
            api_url: URL of the price API endpoint
            timeout: Request timeout in seconds
            currency: Currency to check price in (e.g., usd, eur, gbp)
        """
        self.api_url = api_url
        if timeout <= 0:
            raise ConfigurationError("Timeout must be greater than zero")
        self.timeout = timeout
        self.currency = currency.lower()

    def get_bitcoin_price(self) -> float:
        """
        Fetch the current Bitcoin price from the API.

        Returns:
            Current Bitcoin price as a float

        Raises:
            requests.RequestException: If API request fails
            KeyError: If response format is unexpected
            ValueError: If price cannot be parsed
        """
        params = {"ids": "bitcoin", "vs_currencies": self.currency}

        response = requests.get(
            self.api_url,
            params=params,
            timeout=self.timeout,
            headers={"Accept": "application/json"},
        )
        response.raise_for_status()

        data = response.json()
        if not isinstance(data, dict) or not isinstance(data.get("bitcoin"), dict):
            raise ValueError("Expected a Bitcoin price object")
        return parse_price(data["bitcoin"][self.currency])

    def check_thresholds(
        self,
        price: float,
        warning_low: float | None = None,
        warning_high: float | None = None,
        critical_low: float | None = None,
        critical_high: float | None = None,
    ) -> ThresholdResult:
        """
        Check price against warning and critical thresholds.

        Args:
            price: Current Bitcoin price
            warning_low: Warning if price drops below this value
            warning_high: Warning if price rises above this value
            critical_low: Critical if price drops below this value
            critical_high: Critical if price rises above this value

        Returns:
            ThresholdResult with status code and message
        """
        price = parse_price(price)
        validate_thresholds(warning_low, warning_high)
        validate_thresholds(critical_low, critical_high)
        currency_upper = self.currency.upper()

        # Critical always takes precedence over warning, including overlapping bounds.
        for status, label, low, high in (
            (CRITICAL, "CRITICAL", critical_low, critical_high),
            (WARNING, "WARNING", warning_low, warning_high),
        ):
            if low is not None and price < low:
                direction, bound = "below", low
            elif high is not None and price > high:
                direction, bound = "above", high
            else:
                continue
            return ThresholdResult(
                status,
                f"{label} - Bitcoin price {price:.2f} {currency_upper} is {direction} "
                f"{label.lower()} threshold {bound:.2f} {currency_upper}",
            )

        return ThresholdResult(
            OK, f"OK - Bitcoin price is {price:.2f} {currency_upper}"
        )


def parse_args(args: list | None = None) -> argparse.Namespace:
    """
    Parse command line arguments.

    Args:
        args: List of arguments (defaults to sys.argv[1:])

    Returns:
        Parsed arguments namespace
    """
    parser = PluginArgumentParser(
        description="Nagios plugin to check Bitcoin price",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
    Check Bitcoin price without thresholds (always returns OK)

  %(prog)s -w 30000:50000 -c 25000:60000
    Warning if price is below 30000 or above 50000
    Critical if price is below 25000 or above 60000

  %(prog)s --warning-low 30000 --critical-low 25000
    Only alert on price drops

  %(prog)s --currency eur
    Check price in EUR instead of USD
        """,
    )

    parser.add_argument(
        "-w",
        "--warning",
        type=str,
        help="Warning threshold range (format: LOW:HIGH)",
    )
    parser.add_argument(
        "-c",
        "--critical",
        type=str,
        help="Critical threshold range (format: LOW:HIGH)",
    )
    parser.add_argument(
        "--warning-low",
        type=float,
        help="Warning threshold for low price",
    )
    parser.add_argument(
        "--warning-high",
        type=float,
        help="Warning threshold for high price",
    )
    parser.add_argument(
        "--critical-low",
        type=float,
        help="Critical threshold for low price",
    )
    parser.add_argument(
        "--critical-high",
        type=float,
        help="Critical threshold for high price",
    )
    parser.add_argument(
        "--currency",
        type=str,
        default=DEFAULT_CURRENCY,
        help=f"Currency to check price in (default: {DEFAULT_CURRENCY})",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"API request timeout in seconds (default: {DEFAULT_TIMEOUT})",
    )
    parser.add_argument(
        "--api-url",
        type=str,
        default=DEFAULT_API_URL,
        help="Custom API URL (default: CoinGecko API)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s 1.0.0",
    )

    return parser.parse_args(args)


def parse_range(range_str: str) -> tuple[float | None, float | None]:
    """
    Parse a Nagios-style range string.

    Args:
        range_str: Range string in format "LOW:HIGH"

    Returns:
        Tuple of (low, high) values

    Raises:
        ValueError: If range format is invalid
    """
    if ":" not in range_str:
        raise ConfigurationError("Invalid range format. Expected LOW:HIGH")

    parts = range_str.split(":")
    if len(parts) != 2:
        raise ConfigurationError("Invalid range format. Expected LOW:HIGH")

    try:
        low = float(parts[0]) if parts[0] else None
        high = float(parts[1]) if parts[1] else None
    except ValueError as exc:
        raise ConfigurationError("Range bounds must be numbers") from exc
    validate_thresholds(low, high)

    return low, high


def resolve_thresholds(
    range_str: str | None, low: float | None, high: float | None
) -> tuple[float | None, float | None]:
    """Merge range bounds with individual options, then validate the result."""
    if range_str is not None:
        range_low, range_high = parse_range(range_str)
        low = range_low if range_low is not None else low
        high = range_high if range_high is not None else high
    validate_thresholds(low, high)
    return low, high


def main(args: list | None = None) -> int:
    """
    Main entry point for the plugin.

    Args:
        args: Command line arguments (defaults to sys.argv[1:])

    Returns:
        Nagios exit code
    """
    try:
        parsed_args = parse_args(args)

        warning_low, warning_high = resolve_thresholds(
            parsed_args.warning, parsed_args.warning_low, parsed_args.warning_high
        )
        critical_low, critical_high = resolve_thresholds(
            parsed_args.critical, parsed_args.critical_low, parsed_args.critical_high
        )

        # Create checker and get price
        checker = BitcoinPriceChecker(
            api_url=parsed_args.api_url,
            timeout=parsed_args.timeout,
            currency=parsed_args.currency,
        )

        if parsed_args.verbose:
            print("Fetching Bitcoin price...", file=sys.stderr)

        price = checker.get_bitcoin_price()

        # Check thresholds
        result = checker.check_thresholds(
            price=price,
            warning_low=warning_low,
            warning_high=warning_high,
            critical_low=critical_low,
            critical_high=critical_high,
        )

        # Output with performance data
        perfdata = f"bitcoin_price={price:.2f}"
        print(f"{result.message} | {perfdata}")

        return result.status

    except ConfigurationError as e:
        print(f"UNKNOWN - Invalid configuration: {e}")
        return UNKNOWN
    except requests.Timeout:
        print("UNKNOWN - API request timed out")
        return UNKNOWN
    except requests.RequestException as e:
        print(f"UNKNOWN - API request failed: {e}")
        return UNKNOWN
    except (KeyError, ValueError) as e:
        print(f"UNKNOWN - Failed to parse API response: {e}")
        return UNKNOWN
    except Exception as e:
        print(f"UNKNOWN - Unexpected error: {e}")
        return UNKNOWN


if __name__ == "__main__":
    sys.exit(main())
