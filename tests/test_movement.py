# SPDX-FileCopyrightText: 2026 Thomas Vincent
# SPDX-License-Identifier: MIT

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

import pytest
import requests
import responses

from check_bitcoin_price import movement
from check_bitcoin_price.plugin import DEFAULT_API_URL, main


@responses.activate
def test_window_severity_and_elapsed_time(tmp_path, monkeypatch, capsys):
    path = tmp_path / "state"
    args = [
        "--state-file",
        str(path),
        "--move-window",
        "900",
        "--warning-move",
        "3",
        "--critical-move",
        "6",
    ]
    for stamp, price, extra, status, text, metric in [
        (1000, 100, [], 0, "baseline pending", "U"),
        (1005, 103, [], 0, "move=+3.00% over 5s", "3.00"),
        (1010, 96, [], 1, "10s change -4.00%", "-4.00"),
        (1900, 92, [], 2, "900s change -8.00%", "-8.00"),
        (2900, 100, ["--warning-high", "90"], 1, "baseline pending", "U"),
        (2910, 102, ["--critical-low", "110"], 2, "102.00 USD is below", "2.00"),
    ]:
        monkeypatch.setattr(movement.time, "time", lambda now=stamp: now)
        responses.upsert(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": price, "last_updated_at": stamp}},
        )
        assert main(args + extra) == status
        out = capsys.readouterr().out
        assert text in out
        assert f"bitcoin_move_window={metric}%;-3:3;-6:6;;" in out


@pytest.mark.parametrize(
    "content",
    ["garbage", "[]", '{"usd":[["bad",1]]}', '{"usd":[[1,-1]]}', '{"usd":null}'],
)
def test_recover_history(tmp_path, content):
    path = tmp_path / "state"
    path.write_text(content)
    assert movement.record_price(path, "usd", 60, 100, 0) == (None, 0)
    assert movement.record_price(path, "usd", 60, 110, 100) == (None, 0)
    assert movement.record_price(path, "eur", 60, 111, 80) == (None, 0)
    assert movement.record_price(path, "usd", 60, 120, 105) == (5, 10)
    assert movement.record_price(path, "usd", 60, 120, 110) == (10, 10)
    assert len(json.loads(path.read_text())["usd"]) == 3


def test_concurrent_state_updates(tmp_path):
    path = tmp_path / "state"
    start = Barrier(4)

    def update(stamp):
        start.wait(timeout=2)
        movement.record_price(path, "usd", 60, stamp, stamp)

    with ThreadPoolExecutor(max_workers=4) as workers:
        list(workers.map(update, range(1, 5)))
    assert json.loads(path.read_text())["usd"] == [[s, s] for s in range(1, 5)]


@responses.activate
def test_bad_state_path_and_missing_timestamp(tmp_path, capsys):
    args = ["--state-file", str(tmp_path / "missing" / "quotes")]
    responses.add(responses.GET, DEFAULT_API_URL, json={"bitcoin": {"usd": 100}})
    responses.add(
        responses.GET,
        DEFAULT_API_URL,
        json={"bitcoin": {"usd": 100, "last_updated_at": movement.time.time()}},
    )
    assert main(args) == 3
    assert "timestamp" in capsys.readouterr().out
    assert main(args) == 3
    assert "history" in capsys.readouterr().out


@pytest.mark.parametrize(
    "args",
    [
        ["--warning-move", "3"],
        ["--state-file", "state", "--max-age", "inf"],
        ["--state-file", "state", "--max-age", "nan"],
        ["--move-window", "0", "--state-file", "state"],
        ["--state-file", "state", "--warning-move", "5", "--critical-move", "1"],
    ],
)
def test_invalid_options(args, capsys):
    assert main(args) == 3
    assert "Invalid configuration" in capsys.readouterr().out


def test_history_overflow_and_failed_replacement(tmp_path, monkeypatch):
    path = tmp_path / "state"
    movement.record_price(path, "usd", 60, 1, sys.float_info.min)
    with pytest.raises(ValueError, match="cannot be represented"):
        movement.record_price(path, "usd", 60, 2, sys.float_info.max)
    contents = path.read_bytes()

    def fail(*args):
        raise OSError("disk full")

    monkeypatch.setattr(movement.os, "replace", fail)
    with pytest.raises(OSError):
        movement.record_price(path, "usd", 60, 3, 10)
    assert path.read_bytes() == contents
    assert set(tmp_path.iterdir()) == {path, tmp_path / "state.lock"}


@responses.activate
@pytest.mark.parametrize(
    "error", [requests.exceptions.SSLError("private"), 401, 503, None]
)
def test_ordered_failover(error, capsys):
    second = "https://second.test/quote"
    third = "https://third.test/quote"
    args = ["--fallback-url", second, "--fallback-url", third, "--retries", "0"]
    if error is None:
        responses.add(responses.GET, DEFAULT_API_URL, json={"bitcoin": {"usd": 100}})
    elif isinstance(error, Exception):
        responses.add(responses.GET, DEFAULT_API_URL, body=error)
    else:
        responses.add(responses.GET, DEFAULT_API_URL, status=error)
    responses.add(responses.GET, second, body=requests.ConnectionError("private"))
    responses.add(responses.GET, third, json={"bitcoin": {"usd": 99}})
    status = main(args)
    output = capsys.readouterr().out
    if error in (None, 503):
        assert status == 0
        assert ("source=primary" if error is None else "source=fallback2") in output
    else:
        assert status == 3
        assert "private" not in output
        assert len(responses.calls) == 1


def test_busy_state_file_has_a_bounded_wait(tmp_path):
    import fcntl

    path = tmp_path / "state"
    with (tmp_path / "state.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with pytest.raises(BlockingIOError):
            movement.record_price(path, "usd", 60, 10, 10)
    assert not path.exists()
