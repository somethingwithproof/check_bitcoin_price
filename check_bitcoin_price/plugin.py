#!/usr/bin/env python3
"""
Nagios plugin to check Bitcoin price.

This plugin fetches the current Bitcoin price from a public API
and returns appropriate Nagios status codes based on configured thresholds.
"""

import argparse
import math
import sys
import time
from typing import NamedTuple, Never

import requests

from check_bitcoin_price.quotes import PriceQuote, parse_price, parse_quote
from check_bitcoin_price.transport import fetch_json

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


class ThresholdResult(NamedTuple):
    """Result of threshold check."""

    status: int
    message: str


class BitcoinPriceChecker:
    """Class to check Bitcoin price against thresholds."""

    def __init__(
        self,
        api_url: str = DEFAULT_API_URL,
        timeout: float = DEFAULT_TIMEOUT,
        currency: str = DEFAULT_CURRENCY,
        retries: int = 1,
        max_age: float | None = None,
    ):
        """
        Initialize the Bitcoin price checker.

        Args:
            api_url: URL of the price API endpoint
            timeout: Request timeout in seconds
            currency: Currency to check price in (e.g., usd, eur, gbp)
        """
        self.api_url = api_url
        if not math.isfinite(timeout) or timeout <= 0:
            raise ConfigurationError("Timeout must be finite and greater than zero")
        if not 0 <= retries <= 5:
            raise ConfigurationError("Retries must be between zero and five")
        if max_age is not None and (not math.isfinite(max_age) or max_age <= 0):
            raise ConfigurationError("Maximum age must be finite and greater than zero")
        self.timeout = timeout
        self.currency = currency.lower()
        self.retries = retries
        self.max_age = max_age

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
        return self.get_quote().price

    def get_quote(self, require_change: bool = False) -> PriceQuote:
        """Retrieve a quote under a single deadline, including retries."""
        params = {
            "ids": "bitcoin",
            "vs_currencies": self.currency,
            "include_last_updated_at": "true",
        }
        if require_change:
            params["include_24hr_change"] = "true"
        started = time.monotonic()
        data = fetch_json(self.api_url, params, self.timeout, self.retries)
        return parse_quote(
            data,
            self.currency,
            time.monotonic() - started,
            self.max_age,
            require_change,
        )

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
    Check Bitcoin price without thresholds (valid quotes return OK)

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
        type=float,
        default=DEFAULT_TIMEOUT,
        help=f"Total request/retry deadline in seconds (default: {DEFAULT_TIMEOUT})",
    )
    parser.add_argument(
        "--retries", type=int, default=1, help="Transient retries (0-5; default: 1)"
    )
    parser.add_argument(
        "--max-age",
        type=float,
        help="Maximum quote age in seconds; require vendor timestamp",
    )
    parser.add_argument(
        "--warning-change",
        type=float,
        help="Warn when absolute 24-hour change exceeds this percentage",
    )
    parser.add_argument(
        "--critical-change",
        type=float,
        help="Critical when absolute 24-hour change exceeds this percentage",
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


def check_change(
    change: float | None, warning: float | None, critical: float | None
) -> ThresholdResult:
    """Alert on the magnitude of signed daily movement."""
    for status, label, limit in (
        (CRITICAL, "CRITICAL", critical),
        (WARNING, "WARNING", warning),
    ):
        if change is not None and limit is not None and abs(change) > limit:
            return ThresholdResult(
                status,
                f"{label} - Bitcoin 24-hour change {change:+.2f}% exceeds "
                f"{label.lower()} limit {limit:g}%",
            )
    return ThresholdResult(OK, "OK")


def performance_range(low: float | None, high: float | None) -> str:
    """Represent existing price bounds using Nagios range syntax."""
    if low is None and high is None:
        return ""
    upper = f"{high:g}" if high is not None else ""
    return f"{low if low is not None else 0:g}:{upper}"


def performance_data(
    quote: PriceQuote,
    warning: tuple[float | None, float | None],
    critical: tuple[float | None, float | None],
    warning_change: float | None,
    critical_change: float | None,
) -> str:
    """Expose price bounds, request time, quote age, and daily-change ranges."""
    metrics = [
        f"bitcoin_price={quote.price:.2f};{performance_range(*warning)};"
        f"{performance_range(*critical)};0;",
        f"request_time={quote.request_seconds:.3f}s;;;0;",
    ]
    if quote.age_seconds is not None:
        metrics.append(f"price_age={quote.age_seconds:.3f}s;;;0;")
    if quote.change_24h is not None:
        change_warning = (
            f"{-warning_change:g}:{warning_change:g}"
            if warning_change is not None
            else ""
        )
        change_critical = (
            f"{-critical_change:g}:{critical_change:g}"
            if critical_change is not None
            else ""
        )
        metrics.append(
            f"bitcoin_change_24h={quote.change_24h:.2f}%;{change_warning};{change_critical};;"
        )
    return " ".join(metrics)


def run_check(parsed_args: argparse.Namespace) -> ThresholdResult:
    """Validate configuration, fetch once, and evaluate all requested metrics."""
    warning = resolve_thresholds(
        parsed_args.warning, parsed_args.warning_low, parsed_args.warning_high
    )
    critical = resolve_thresholds(
        parsed_args.critical, parsed_args.critical_low, parsed_args.critical_high
    )
    validate_thresholds(parsed_args.warning_change, parsed_args.critical_change)
    checker = BitcoinPriceChecker(
        api_url=parsed_args.api_url,
        timeout=parsed_args.timeout,
        currency=parsed_args.currency,
        retries=parsed_args.retries,
        max_age=parsed_args.max_age,
    )
    if parsed_args.verbose:
        print("Fetching Bitcoin price...", file=sys.stderr)
    require_change = (
        parsed_args.warning_change is not None
        or parsed_args.critical_change is not None
    )
    quote = checker.get_quote(require_change)
    price_result = checker.check_thresholds(quote.price, *warning, *critical)
    change_result = check_change(
        quote.change_24h, parsed_args.warning_change, parsed_args.critical_change
    )
    result = (
        change_result if change_result.status > price_result.status else price_result
    )
    perfdata = performance_data(
        quote,
        warning,
        critical,
        parsed_args.warning_change,
        parsed_args.critical_change,
    )
    return ThresholdResult(result.status, f"{result.message} | {perfdata}")


def main(args: list | None = None) -> int:
    """
    Main entry point for the plugin.

    Args:
        args: Command line arguments (defaults to sys.argv[1:])

    Returns:
        Nagios exit code
    """
    try:
        result = run_check(parse_args(args))
        print(result.message)
        return result.status

    except ConfigurationError as e:
        print(f"UNKNOWN - Invalid configuration: {e}")
        return UNKNOWN
    except requests.Timeout:
        print("UNKNOWN - API request timed out")
        return UNKNOWN
    except requests.RequestException as e:
        detail = (
            f"HTTP {e.response.status_code}"
            if e.response is not None
            else type(e).__name__
        )
        # Exception strings may contain credentials embedded in a custom URL.
        print(f"UNKNOWN - API request failed: {detail}")
        return UNKNOWN
    except (KeyError, ValueError) as e:
        print(f"UNKNOWN - Failed to parse API response: {e}")
        return UNKNOWN
    except Exception as e:
        print(f"UNKNOWN - Unexpected error: {e}")
        return UNKNOWN


if __name__ == "__main__":
    sys.exit(main())
