#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025-2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

"""
Nagios plugin to check Bitcoin price.

This plugin fetches the current Bitcoin price from a public API
and returns appropriate Nagios status codes based on configured thresholds.
"""

import argparse
import math
import re
import sys
import time
from pathlib import Path
from typing import NamedTuple, Never

import requests

from check_bitcoin_price import __version__
from check_bitcoin_price.i18n import set_locale, t
from check_bitcoin_price.movement import OutOfOrderSampleError, record_price
from check_bitcoin_price.quotes import (
    PriceQuote,
    parse_price,
    parse_quote,
    plain_number,
)
from check_bitcoin_price.transport import RETRYABLE_STATUS, fetch_json

# Nagios exit codes
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

# Default API endpoint (CoinGecko - free, no API key required)
DEFAULT_API_URL = "https://api.coingecko.com/api/v3/simple/price"
DEFAULT_TIMEOUT = 10
DEFAULT_CURRENCY = "usd"
# Applies to quotes that carry a vendor timestamp when --max-age is not given.
DEFAULT_MAX_AGE = 3600
# A looser pattern would let names such as last_updated_at select metadata.
CURRENCY_CODE = re.compile(r"[a-z0-9]{2,16}", re.ASCII)


class ConfigurationError(ValueError):
    """Invalid monitoring check configuration."""


class MovementStateError(Exception):
    """Movement history could not be read, ordered, or updated."""


class PluginArgumentParser(argparse.ArgumentParser):
    """Report invalid arguments as UNKNOWN rather than CRITICAL (exit 2)."""

    def error(self, message: str) -> Never:
        raise ConfigurationError(message)


def validate_thresholds(
    low: float | None,
    high: float | None,
    ordering: str | None = None,
) -> None:
    """Require finite, nonnegative bounds in ascending order."""
    for value in (low, high):
        if value is not None and (not math.isfinite(value) or value < 0):
            raise ConfigurationError(t("config.thresholds_nonnegative"))
    if low is not None and high is not None and low > high:
        raise ConfigurationError(ordering or t("config.low_exceeds_high"))


def may_succeed_elsewhere(error: requests.RequestException) -> bool:
    """Whether a fallback source is worth trying after this failure."""
    if isinstance(error, requests.HTTPError):
        return (
            error.response is not None
            and error.response.status_code in RETRYABLE_STATUS
        )
    # A certificate failure is reported, not masked by a working fallback.
    if isinstance(error, requests.exceptions.SSLError):
        return False
    return isinstance(error, (requests.ConnectionError, requests.Timeout))


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
        fallback_urls: tuple[str, ...] = (),
    ):
        """
        Initialize the Bitcoin price checker.

        Args:
            api_url: URL of the price API endpoint
            timeout: Request timeout in seconds
            currency: Currency to check price in (e.g., usd, eur, gbp)
            retries: Additional attempts after a transient failure (0-5)
            max_age: Maximum quote age in seconds; requires a vendor timestamp.
                When None, timestamped quotes are limited to DEFAULT_MAX_AGE.
        """
        self.api_url = api_url
        self.fallback_urls = fallback_urls
        self.source = "primary"
        if not math.isfinite(timeout) or timeout <= 0:
            raise ConfigurationError(t("config.timeout_positive"))
        if not 0 <= retries <= 5:
            raise ConfigurationError(t("config.retries_range"))
        if max_age is not None and (not math.isfinite(max_age) or max_age <= 0):
            raise ConfigurationError(t("config.max_age_positive"))
        self.timeout = timeout
        self.currency = currency.lower()
        if CURRENCY_CODE.fullmatch(self.currency) is None:
            raise ConfigurationError(t("config.currency_format"))
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
        data = self.fetch_from_sources(params, started + self.timeout)
        return parse_quote(
            data,
            self.currency,
            time.monotonic() - started,
            DEFAULT_MAX_AGE if self.max_age is None else self.max_age,
            require_change,
            require_timestamp=self.max_age is not None,
        )

    def fetch_from_sources(self, params: dict[str, str], deadline: float) -> object:
        """Try each source in order until one answers or fails permanently."""
        sources = (self.api_url, *self.fallback_urls)
        for index, url in enumerate(sources):
            self.source = f"fallback{index}" if index else "primary"
            now = time.monotonic()
            # A slow endpoint can consume only its share of the remaining time.
            share = (deadline - now) / (len(sources) - index)
            try:
                return fetch_json(
                    url, params, share, self.retries, deadline=now + share
                )
            except requests.RequestException as exc:
                if index == len(sources) - 1 or not may_succeed_elsewhere(exc):
                    raise
        raise AssertionError("unreachable")  # pragma: no cover

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
        for status, level, low, high in (
            (CRITICAL, "critical", critical_low, critical_high),
            (WARNING, "warning", warning_low, warning_high),
        ):
            if low is not None and price < low:
                direction, bound = "below", low
            elif high is not None and price > high:
                direction, bound = "above", high
            else:
                continue
            return ThresholdResult(
                status,
                t(
                    f"status.price_{direction}_{level}",
                    price=f"{price:.2f}",
                    bound=f"{bound:.2f}",
                    currency=currency_upper,
                ),
            )

        return ThresholdResult(
            OK,
            t("status.price_ok", price=f"{price:.2f}", currency=currency_upper),
        )


def _extract_lang(args: list[str] | None) -> str | None:
    """Read --lang before argparse runs so --help uses the requested locale."""
    raw = sys.argv[1:] if args is None else args
    for idx, arg in enumerate(raw):
        if arg == "--lang" and idx + 1 < len(raw):
            return str(raw[idx + 1])
        if isinstance(arg, str) and arg.startswith("--lang="):
            return arg.split("=", 1)[1]
    return None


def parse_args(args: list | None = None) -> argparse.Namespace:
    """
    Parse command line arguments.

    Args:
        args: List of arguments (defaults to sys.argv[1:])

    Returns:
        Parsed arguments namespace
    """
    set_locale(_extract_lang(args))
    parser = PluginArgumentParser(
        description=t("cli.description"),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="\n" + t("cli.epilog") + "\n        ",
    )

    parser.add_argument(
        "-w",
        "--warning",
        type=str,
        help=t("cli.warning_help"),
    )
    parser.add_argument(
        "-c",
        "--critical",
        type=str,
        help=t("cli.critical_help"),
    )
    parser.add_argument(
        "--warning-low",
        type=float,
        help=t("cli.warning_low_help"),
    )
    parser.add_argument(
        "--warning-high",
        type=float,
        help=t("cli.warning_high_help"),
    )
    parser.add_argument(
        "--critical-low",
        type=float,
        help=t("cli.critical_low_help"),
    )
    parser.add_argument(
        "--critical-high",
        type=float,
        help=t("cli.critical_high_help"),
    )
    parser.add_argument(
        "--currency",
        type=str,
        default=DEFAULT_CURRENCY,
        help=t("cli.currency_help", default=DEFAULT_CURRENCY),
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help=t("cli.timeout_help", default=DEFAULT_TIMEOUT),
    )
    parser.add_argument("--retries", type=int, default=1, help=t("cli.retries_help"))
    parser.add_argument(
        "--max-age",
        type=float,
        help=t("cli.max_age_help", default=DEFAULT_MAX_AGE),
    )
    parser.add_argument(
        "--warning-change",
        type=float,
        help=t("cli.warning_change_help"),
    )
    parser.add_argument(
        "--critical-change",
        type=float,
        help=t("cli.critical_change_help"),
    )
    parser.add_argument(
        "--api-url",
        type=str,
        default=DEFAULT_API_URL,
        help=t("cli.api_url_help"),
    )
    parser.add_argument(
        "--fallback-url",
        action="append",
        default=[],
        help=t("cli.fallback_url_help"),
    )
    parser.add_argument("--state-file", type=Path, help=t("cli.state_file_help"))
    parser.add_argument("--move-window", type=float, help=t("cli.move_window_help"))
    parser.add_argument(
        "--warning-move",
        type=float,
        help=t("cli.warning_move_help"),
    )
    parser.add_argument(
        "--critical-move",
        type=float,
        help=t("cli.critical_move_help"),
    )
    parser.add_argument(
        "--lang",
        type=str,
        default=None,
        help=t("cli.lang_help"),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help=t("cli.verbose_help"),
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    parsed = parser.parse_args(args)
    set_locale(parsed.lang)
    return parsed


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
        raise ConfigurationError(t("config.invalid_range_format"))

    parts = range_str.split(":")
    if len(parts) != 2:
        raise ConfigurationError(t("config.invalid_range_format"))

    try:
        low = float(parts[0]) if parts[0] else None
        high = float(parts[1]) if parts[1] else None
    except ValueError as exc:
        raise ConfigurationError(t("config.range_bounds_numbers")) from exc
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
    change: float | None,
    warning: float | None,
    critical: float | None,
    label_period: str = "24-hour",
) -> ThresholdResult:
    """Alert on the magnitude of signed movement over the given period."""
    for status, key, limit in (
        (CRITICAL, "status.change_critical", critical),
        (WARNING, "status.change_warning", warning),
    ):
        if change is not None and limit is not None and abs(change) > limit:
            return ThresholdResult(
                status,
                t(
                    key,
                    period=label_period,
                    change=f"{change:+.2f}",
                    limit=plain_number(limit),
                ),
            )
    return ThresholdResult(OK, "OK")


def performance_range(low: float | None, high: float | None) -> str:
    """Represent existing price bounds using Nagios range syntax."""
    if low is None and high is None:
        return ""
    upper = plain_number(high) if high is not None else ""
    return f"{plain_number(low if low is not None else 0)}:{upper}"


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
        metrics.append(
            change_metric(
                "bitcoin_change_24h", quote.change_24h, warning_change, critical_change
            )
        )
    return " ".join(metrics)


def change_metric(
    name: str, change: float | None, warning: float | None, critical: float | None
) -> str:
    value = "U" if change is None else f"{change:.2f}"
    warn, crit = (
        "" if limit is None else f"{plain_number(-limit)}:{plain_number(limit)}"
        for limit in (warning, critical)
    )
    return f"{name}={value}%;{warn};{crit};;"


def movement_window(parsed_args: argparse.Namespace) -> float:
    """Validate the movement options and return the window in seconds."""
    validate_thresholds(
        parsed_args.warning_move,
        parsed_args.critical_move,
        t("config.warning_move_exceeds_critical"),
    )
    move_options = (
        parsed_args.warning_move,
        parsed_args.critical_move,
        parsed_args.move_window,
    )
    if parsed_args.state_file is None and any(x is not None for x in move_options):
        raise ConfigurationError(t("config.movement_requires_state_file"))
    window = 3600.0 if parsed_args.move_window is None else parsed_args.move_window
    if not math.isfinite(window) or window <= 0:
        raise ConfigurationError(t("config.movement_window_positive"))
    return float(window)


def window_movement(
    state_file: Path, currency: str, window: float, timestamp: float, price: float
) -> tuple[float | None, str]:
    """Record the quote; return its movement and the period that covers."""
    try:
        move, elapsed = record_price(state_file, currency, window, timestamp, price)
    except OutOfOrderSampleError as exc:
        raise MovementStateError(t("error.quote_older_than_history")) from exc
    except OSError as exc:
        raise MovementStateError(t("error.cannot_update_history")) from exc
    return move, f"{elapsed:g}s"


def run_check(parsed_args: argparse.Namespace) -> ThresholdResult:
    """Validate configuration, fetch once, and evaluate all requested metrics."""
    warning = resolve_thresholds(
        parsed_args.warning, parsed_args.warning_low, parsed_args.warning_high
    )
    critical = resolve_thresholds(
        parsed_args.critical, parsed_args.critical_low, parsed_args.critical_high
    )
    validate_thresholds(
        parsed_args.warning_change,
        parsed_args.critical_change,
        t("config.warning_change_exceeds_critical"),
    )
    window = movement_window(parsed_args)
    checker = BitcoinPriceChecker(
        api_url=parsed_args.api_url,
        timeout=parsed_args.timeout,
        currency=parsed_args.currency,
        retries=parsed_args.retries,
        max_age=parsed_args.max_age,
        fallback_urls=tuple(parsed_args.fallback_url),
    )
    if parsed_args.state_file is not None:
        # Movement needs a timestamp inside the window, but a long window must
        # not loosen the default age limit.
        limit = DEFAULT_MAX_AGE if checker.max_age is None else checker.max_age
        checker.max_age = min(limit, window)
    if parsed_args.verbose:
        print(t("status.fetching"), file=sys.stderr)
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
    details = []
    if checker.fallback_urls:
        details.append(f"source={checker.source}")
        if parsed_args.verbose:
            print(
                t("status.quote_received_from", source=checker.source), file=sys.stderr
            )
    if parsed_args.state_file is not None and quote.timestamp is not None:
        move, period = window_movement(
            parsed_args.state_file,
            checker.currency,
            window,
            quote.timestamp,
            quote.price,
        )
        window_result = check_change(
            move, parsed_args.warning_move, parsed_args.critical_move, period
        )
        if window_result.status > result.status:
            result = window_result
        elif move is None:
            details.append(t("status.movement_baseline_pending"))
        else:
            details.append(t("status.move_detail", move=f"{move:+.2f}", period=period))
        perfdata += " " + change_metric(
            "bitcoin_move_window",
            move,
            parsed_args.warning_move,
            parsed_args.critical_move,
        )
    return ThresholdResult(
        result.status, " ".join([result.message, *details]) + f" | {perfdata}"
    )


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
        print(t("error.invalid_configuration", error=e))
        return UNKNOWN
    except MovementStateError as e:
        print(f"UNKNOWN - {e}")
        return UNKNOWN
    except requests.Timeout:
        print(t("error.api_timeout"))
        return UNKNOWN
    except requests.RequestException as e:
        detail = (
            f"HTTP {e.response.status_code}"
            if e.response is not None
            else type(e).__name__
        )
        # Exception strings may contain credentials embedded in a custom URL.
        print(t("error.api_request_failed", detail=detail))
        return UNKNOWN
    except (KeyError, ValueError) as e:
        print(t("error.parse_failed", error=e))
        return UNKNOWN
    except Exception as e:
        print(t("error.unexpected", error=e))
        return UNKNOWN


if __name__ == "__main__":
    sys.exit(main())
