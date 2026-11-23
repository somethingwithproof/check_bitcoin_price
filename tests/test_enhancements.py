# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

"""Operational regression tests for freshness, movement, and retry budgets."""

import time
from datetime import UTC, datetime
from email.utils import format_datetime
from threading import Event

import pytest
import requests
import responses

from check_bitcoin_price import quotes, transport
from check_bitcoin_price.plugin import (
    CRITICAL,
    DEFAULT_API_URL,
    OK,
    UNKNOWN,
    WARNING,
    BitcoinPriceChecker,
    main,
)


@pytest.fixture
def instant_backoff(monkeypatch):
    monkeypatch.setattr(transport, "retry_delay", lambda response, attempt: 0.0)


@pytest.mark.parametrize("age, expected", [(0, OK), (300, OK), (301, UNKNOWN)])
@responses.activate
def test_freshness_boundary(age, expected, monkeypatch, capsys):
    monkeypatch.setattr(quotes.time, "time", lambda: 2_000_000_000)
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"usd": 40000, "last_updated_at": 2_000_000_000 - age}},
    )
    assert main(["--max-age", "300"]) == expected
    output = capsys.readouterr().out
    if expected == UNKNOWN:
        assert "stale" in output
        assert "bitcoin_price=" not in output
    else:
        assert f"price_age={age:.3f}s" in output
    assert "include_last_updated_at=true" in responses.calls[0].request.url


@pytest.mark.parametrize("timestamp", [None, True, 0, -1, "bad", "inf", 10**400])
@responses.activate
def test_unusable_timestamp_is_unknown(timestamp, capsys):
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"usd": 40000, "last_updated_at": timestamp}},
    )
    assert main(["--max-age", "300"]) == UNKNOWN
    assert "bitcoin_price=" not in capsys.readouterr().out


@responses.activate
def test_future_timestamp_is_unknown(monkeypatch, capsys):
    monkeypatch.setattr(quotes.time, "time", lambda: 2_000_000_000)
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"usd": 40000, "last_updated_at": 2_000_000_060}},
    )
    assert main(["--max-age", "300"]) == UNKNOWN
    assert "future" in capsys.readouterr().out


@pytest.mark.parametrize(
    "change, expected",
    [
        (0, OK),
        (5, OK),
        (-5, OK),
        (6, WARNING),
        (-6, WARNING),
        (10, WARNING),
        (-11, CRITICAL),
        (11, CRITICAL),
    ],
)
@responses.activate
def test_signed_change_alerts(change, expected, capsys):
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"usd": 40000, "usd_24h_change": change}},
    )
    assert main(["--warning-change", "5", "--critical-change", "10"]) == expected
    output = capsys.readouterr().out
    assert f"bitcoin_change_24h={change:.2f}%;-5:5;-10:10;;" in output
    assert "include_24hr_change=true" in responses.calls[0].request.url


@pytest.mark.parametrize("change", [None, True, [], "nan", "inf"])
@responses.activate
def test_required_change_is_unusable(change, capsys):
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"usd": 40000, "usd_24h_change": change}},
    )
    assert main(["--warning-change", "5"]) == UNKNOWN
    assert "bitcoin_price=" not in capsys.readouterr().out


@responses.activate
def test_change_matches_selected_currency(capsys):
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"eur": 40000, "eur_24h_change": -12, "usd_24h_change": 0}},
    )
    assert main(["--currency", "EUR", "--critical-change", "10"]) == CRITICAL
    assert "-12.00%" in capsys.readouterr().out


@pytest.mark.parametrize(
    "price, change, expected, message",
    [
        (28000, 12, CRITICAL, "24-hour change"),
        (20000, 6, CRITICAL, "price"),
        (40000, 0, OK, "price"),
    ],
)
@responses.activate
def test_highest_severity_wins(price, change, expected, message, capsys):
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"usd": price, "usd_24h_change": change}},
    )
    args = [
        "--warning-low",
        "30000",
        "--critical-low",
        "25000",
        "--warning-change",
        "5",
        "--critical-change",
        "10",
    ]
    assert main(args) == expected
    assert message in capsys.readouterr().out.split("|")[0]


@responses.activate
def test_threshold_performance_data(capsys):
    responses.add(responses.GET, DEFAULT_API_URL, json={"bitcoin": {"usd": 40000}})
    assert main(["-w", "30000:50000", "-c", "25000:60000"]) == OK
    output = capsys.readouterr().out
    assert "bitcoin_price=40000.00;30000:50000;25000:60000;0;" in output
    assert "request_time=" in output
    assert "price_age=" not in output


@pytest.mark.parametrize("status", [408, 429, 500, 502, 503, 504])
@responses.activate
def test_transient_http_status_recovers(status, instant_backoff):
    responses.add(responses.GET, DEFAULT_API_URL, status=status)
    responses.add(responses.GET, DEFAULT_API_URL, json={"bitcoin": {"usd": 40000}})
    assert BitcoinPriceChecker().get_bitcoin_price() == 40000
    assert len(responses.calls) == 2


@pytest.mark.parametrize("error", [requests.Timeout(), requests.ConnectionError()])
@responses.activate
def test_transient_connection_recovers(error, instant_backoff):
    responses.add(responses.GET, DEFAULT_API_URL, body=error)
    responses.add(responses.GET, DEFAULT_API_URL, json={"bitcoin": {"usd": 40000}})
    assert BitcoinPriceChecker().get_bitcoin_price() == 40000
    assert len(responses.calls) == 2


@pytest.mark.parametrize("status", [400, 401, 403, 404, 501])
@responses.activate
def test_permanent_http_error_is_not_retried(status):
    responses.add(responses.GET, DEFAULT_API_URL, status=status)
    assert main([]) == UNKNOWN
    assert len(responses.calls) == 1


@responses.activate
def test_invalid_json_is_not_retried():
    responses.add(responses.GET, DEFAULT_API_URL, body="invalid json")
    assert main([]) == UNKNOWN
    assert len(responses.calls) == 1


@responses.activate
def test_connection_diagnostics_do_not_echo_url_details(capsys):
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        body=requests.ConnectionError("private-query-value"),
    )
    assert main(["--retries", "0"]) == UNKNOWN
    output = capsys.readouterr().out
    assert "ConnectionError" in output
    assert "private-query-value" not in output


@pytest.mark.parametrize("retries, calls", [(0, 1), (1, 2), (3, 4)])
@responses.activate
def test_retry_count_is_bounded(retries, calls, instant_backoff):
    responses.add(responses.GET, DEFAULT_API_URL, status=503)
    assert main(["--retries", str(retries)]) == UNKNOWN
    assert len(responses.calls) == calls


@responses.activate
def test_retry_after_does_not_exceed_deadline(capsys):
    responses.add(
        responses.GET, DEFAULT_API_URL, status=429, headers={"Retry-After": "60"}
    )
    started = time.monotonic()
    assert main(["--timeout", "0.2"]) == UNKNOWN
    assert time.monotonic() - started < 0.5
    assert len(responses.calls) == 1
    assert "HTTP 429" in capsys.readouterr().out


@responses.activate
def test_unaffordable_backoff_reports_the_connection_failure(capsys):
    responses.add(responses.GET, DEFAULT_API_URL, body=requests.ConnectionError())
    assert main(["--timeout", "0.2"]) == UNKNOWN
    assert len(responses.calls) == 1
    assert "ConnectionError" in capsys.readouterr().out


@pytest.mark.parametrize(
    "header, expected", [("1", 1), ("0", 0), ("-1", 0), ("bad", 0.5), ("inf", 0.5)]
)
def test_retry_after_seconds_and_invalid_values(header, expected):
    response = requests.Response()
    response.headers["Retry-After"] = header
    assert transport.retry_delay(response, 0) == expected


def test_retry_after_http_date(monkeypatch):
    monkeypatch.setattr(transport.time, "time", lambda: 2_000_000_000)
    response = requests.Response()
    response.headers["Retry-After"] = format_datetime(
        datetime.fromtimestamp(2_000_000_030, UTC), usegmt=True
    )
    assert transport.retry_delay(response, 0) == 30


def test_blocked_transport_respects_total_deadline(monkeypatch):
    release, finished = Event(), Event()

    def blocked(*args):
        release.wait(timeout=1)
        finished.set()
        return {}

    monkeypatch.setattr(transport, "fetch_with_retries", blocked)
    try:
        with pytest.raises(requests.Timeout, match="Total timeout expired"):
            transport.fetch_json(DEFAULT_API_URL, {}, 0.02, 0)
    finally:
        release.set()
        assert finished.wait(timeout=1)


def test_expired_budget_never_starts_a_request():
    expired_at = time.monotonic() - 1
    with pytest.raises(requests.Timeout, match="Total timeout expired"):
        transport.fetch_with_retries(DEFAULT_API_URL, {}, expired_at, 1)


@pytest.mark.parametrize(
    "args",
    [
        ["--max-age", "0"],
        ["--max-age", "nan"],
        ["--max-age=-1"],
        ["--timeout", "nan"],
        ["--retries=-1"],
        ["--retries", "6"],
        ["--warning-change=-1"],
        ["--critical-change", "nan"],
        ["--warning-change", "10", "--critical-change", "5"],
        ["--currency", "last_updated_at"],
        ["--currency", "u"],
        ["--currency", ""],
    ],
)
@responses.activate
def test_new_configuration_is_validated_before_requests(args, capsys):
    assert main(args) == UNKNOWN
    assert "Invalid configuration" in capsys.readouterr().out
    assert not responses.calls


def test_change_limit_order_is_named(capsys):
    assert main(["--warning-change", "10", "--critical-change", "5"]) == UNKNOWN
    assert "Warning change must not exceed critical change" in capsys.readouterr().out


@responses.activate
def test_missing_currency_is_named(capsys):
    responses.add(responses.GET, DEFAULT_API_URL, json={"bitcoin": {"usd": 40000}})
    assert main(["--currency", "eur"]) == UNKNOWN
    assert "Response has no EUR price" in capsys.readouterr().out


@pytest.mark.parametrize("age, expected", [(3600, OK), (3601, UNKNOWN)])
@responses.activate
def test_timestamped_quotes_have_a_default_age_limit(
    age, expected, monkeypatch, capsys
):
    monkeypatch.setattr(quotes.time, "time", lambda: 2_000_000_000)
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"usd": 40000, "last_updated_at": 2_000_000_000 - age}},
    )
    assert main([]) == expected
    assert ("stale" in capsys.readouterr().out) == (expected == UNKNOWN)


@pytest.mark.parametrize(
    "price, expected",
    [("40000.5", OK), ("4e4", OK), ("40_000", UNKNOWN), (" 40000", UNKNOWN)],
)
@responses.activate
def test_numeric_strings_must_be_plain_decimals(price, expected):
    responses.add(responses.GET, DEFAULT_API_URL, json={"bitcoin": {"usd": price}})
    assert main([]) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (16250000.0, "16250000"),
        (123456.78, "123456.78"),
        (1e22, "10000000000000000000000"),
        (0.5, "0.5"),
        (-0.0, "0"),
    ],
)
def test_plain_number_avoids_exponents_and_rounding(value, expected):
    assert quotes.plain_number(value) == expected


@responses.activate
def test_large_thresholds_keep_full_precision_in_output(capsys):
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"jpy": 15000000, "jpy_24h_change": 3}},
    )
    args = ["--currency", "jpy", "-w", "14500000:16250000", "--warning-change", "2.5"]
    assert main(args) == WARNING
    output = capsys.readouterr().out
    assert "limit 2.5%" in output
    assert "bitcoin_price=15000000.00;14500000:16250000;;0;" in output
    assert "bitcoin_change_24h=3.00%;-2.5:2.5;;;" in output


@responses.activate
@pytest.mark.parametrize("extra", [0, 1])
def test_response_limit_applies_to_decoded_bytes(extra):
    body = b"{}" + b" " * (transport.MAX_RESPONSE_BYTES - 2 + extra)
    responses.add(responses.GET, DEFAULT_API_URL, body=body)
    if extra:
        with pytest.raises(ValueError, match="exceeds 64 KiB"):
            transport.fetch_json(DEFAULT_API_URL, {}, 1, 0)
    else:
        assert transport.fetch_json(DEFAULT_API_URL, {}, 1, 0) == {}


@responses.activate
def test_deadline_expires_while_reading_body(monkeypatch):
    ticks = iter([0, 1])
    monkeypatch.setattr(transport.time, "monotonic", lambda: next(ticks))
    responses.add(responses.GET, DEFAULT_API_URL, body=b"{}")
    with pytest.raises(requests.Timeout, match="Total timeout expired"):
        transport.fetch_with_retries(DEFAULT_API_URL, {}, 1, 0)


@responses.activate
def test_redirect_is_followed_to_the_quote():
    target = "https://quotes.example.org/price"
    responses.add(
        responses.GET, DEFAULT_API_URL, status=302, headers={"Location": target}
    )
    responses.add(responses.GET, target, json={"bitcoin": {"usd": 40000}})
    assert BitcoinPriceChecker().get_bitcoin_price() == 40000
