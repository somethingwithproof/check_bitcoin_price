# SPDX-FileCopyrightText: 2026 Thomas Vincent
# SPDX-License-Identifier: MIT

"""Windowed price observations for opt-in movement alerts."""

import json
import math
import os
import time
from pathlib import Path
from tempfile import NamedTemporaryFile


def read_history(path: Path) -> dict[str, list[tuple[float, float]]]:
    try:
        raw = json.loads(path.read_bytes())
        if not isinstance(raw, dict):
            return {}
        history: dict[str, list[tuple[float, float]]] = {}
        for currency, rows in raw.items():
            samples = []
            for timestamp, price in rows:
                if (
                    type(timestamp) not in (int, float)
                    or type(price) not in (int, float)
                    or not math.isfinite(timestamp)
                    or not math.isfinite(price)
                    or timestamp <= 0
                    or price < 0
                ):
                    raise ValueError("Invalid price history")
                samples.append((timestamp, price))
            history[currency] = samples
        return history
    except (FileNotFoundError, ValueError, TypeError, OverflowError):
        return {}


def write_history(path: Path, history: dict[str, list[tuple[float, float]]]) -> None:
    with NamedTemporaryFile(
        dir=path.parent, mode="w", encoding="utf-8", delete_on_close=False
    ) as tmp:
        json.dump(history, tmp, allow_nan=False, separators=(",", ":"))
        tmp.close()
        os.replace(tmp.name, path)


def record_price(
    path: Path, currency: str, window: float, timestamp: float, price: float
) -> tuple[float | None, float]:
    """Serialize the read/modify/replace cycle on a stable sibling lock file."""
    import fcntl

    # Replacing the history changes its inode, so it cannot itself be the lock.
    with path.with_name(path.name + ".lock").open("a") as lock:
        deadline = time.monotonic() + 1
        while True:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() >= deadline:
                    raise
                time.sleep(0.01)

        history = read_history(path)
        samples = dict(history.get(currency, []))
        samples[timestamp] = price
        newest = max(samples)
        ordered = sorted((t, p) for t, p in samples.items() if t >= newest - window)
        history[currency] = ordered
        write_history(path, history)
        for start, baseline in ordered:
            if start < timestamp and baseline > 0:
                move = (price - baseline) / baseline * 100
                if not math.isfinite(move):
                    raise ValueError("Window movement cannot be represented")
                return move, timestamp - start
        return None, 0.0
