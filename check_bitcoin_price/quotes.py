"""Validated Bitcoin quotes and optional freshness/change metadata."""

import math
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class PriceQuote:
    """One vendor quote; age and daily change may be unavailable."""

    price: float
    request_seconds: float
    age_seconds: float | None = None
    change_24h: float | None = None


def finite_number(value: object, label: str) -> float:
    """Reject booleans, containers, and nonfinite or overflowing numbers."""
    message = f"{label} must be a finite number"
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        raise ValueError(message)
    try:
        number = float(value)
    except (ValueError, OverflowError) as exc:
        raise ValueError(message) from exc
    if not math.isfinite(number):
        raise ValueError(message)
    return number


def parse_price(price: object) -> float:
    """Normalize a price without allowing invalid data to report OK."""
    value = finite_number(price, "Bitcoin price")
    if value < 0:
        raise ValueError("Bitcoin price must be nonnegative")
    return value


def quote_age(timestamp: object, max_age: float | None) -> float | None:
    """Require a usable vendor timestamp when freshness is enabled."""
    if timestamp is None:
        if max_age is not None:
            raise ValueError("Quote timestamp is missing; freshness cannot be verified")
        return None
    updated_at = finite_number(timestamp, "Quote timestamp")
    age = time.time() - updated_at
    if updated_at <= 0 or age < 0:
        raise ValueError("Quote timestamp must be positive and not in the future")
    if max_age is not None and age > max_age:
        raise ValueError(f"Quote is stale ({age:.1f}s old; maximum {max_age:g}s)")
    return age


def parse_quote(
    data: object,
    currency: str,
    request_seconds: float,
    max_age: float | None = None,
    require_change: bool = False,
) -> PriceQuote:
    """Validate price and metadata before evaluating any alerts."""
    if not isinstance(data, dict) or not isinstance(data.get("bitcoin"), dict):
        raise ValueError("Expected a Bitcoin price object")
    bitcoin = data["bitcoin"]
    price = parse_price(bitcoin[currency])
    age = quote_age(bitcoin.get("last_updated_at"), max_age)
    raw_change = bitcoin.get(f"{currency}_24h_change")
    if raw_change is None and require_change:
        raise ValueError("24-hour change is missing; change alerts cannot be evaluated")
    change = (
        finite_number(raw_change, "24-hour change") if raw_change is not None else None
    )
    return PriceQuote(price, request_seconds, age, change)
