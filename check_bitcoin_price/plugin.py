#!/usr/bin/env python3
"""
Nagios plugin to check Bitcoin price.

This plugin fetches the current Bitcoin price from a public API
and returns appropriate Nagios status codes based on configured thresholds.
"""

import argparse
import sys
from typing import NamedTuple

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
        price = data["bitcoin"][self.currency]

        return float(price)

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
        currency_upper = self.currency.upper()

        # Check critical thresholds first
        if critical_low is not None and price < critical_low:
            return ThresholdResult(
                CRITICAL,
                f"CRITICAL - Bitcoin price {price:.2f} {currency_upper} is below "
                f"critical threshold {critical_low:.2f} {currency_upper}",
            )

        if critical_high is not None and price > critical_high:
            return ThresholdResult(
                CRITICAL,
                f"CRITICAL - Bitcoin price {price:.2f} {currency_upper} is above "
                f"critical threshold {critical_high:.2f} {currency_upper}",
            )

        # Check warning thresholds
        if warning_low is not None and price < warning_low:
            return ThresholdResult(
                WARNING,
                f"WARNING - Bitcoin price {price:.2f} {currency_upper} is below "
                f"warning threshold {warning_low:.2f} {currency_upper}",
            )

        if warning_high is not None and price > warning_high:
            return ThresholdResult(
                WARNING,
                f"WARNING - Bitcoin price {price:.2f} {currency_upper} is above "
                f"warning threshold {warning_high:.2f} {currency_upper}",
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
    parser = argparse.ArgumentParser(
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
        raise ValueError(f"Invalid range format: {range_str}. Expected LOW:HIGH")

    parts = range_str.split(":")
    if len(parts) != 2:
        raise ValueError(f"Invalid range format: {range_str}. Expected LOW:HIGH")

    low = float(parts[0]) if parts[0] else None
    high = float(parts[1]) if parts[1] else None

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

        # Parse threshold ranges if provided
        warning_low = parsed_args.warning_low
        warning_high = parsed_args.warning_high
        critical_low = parsed_args.critical_low
        critical_high = parsed_args.critical_high

        if parsed_args.warning:
            w_low, w_high = parse_range(parsed_args.warning)
            warning_low = w_low if w_low is not None else warning_low
            warning_high = w_high if w_high is not None else warning_high

        if parsed_args.critical:
            c_low, c_high = parse_range(parsed_args.critical)
            critical_low = c_low if c_low is not None else critical_low
            critical_high = c_high if c_high is not None else critical_high

        # Create checker and get price
        checker = BitcoinPriceChecker(
            api_url=parsed_args.api_url,
            timeout=parsed_args.timeout,
            currency=parsed_args.currency,
        )

        if parsed_args.verbose:
            print(f"Fetching Bitcoin price from {parsed_args.api_url}...")

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
