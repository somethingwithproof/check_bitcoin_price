# SPDX-FileCopyrightText: 2026 Thomas Vincent
# SPDX-License-Identifier: MIT

"""Windowed price observations for opt-in movement alerts."""

import errno
import json
import math
import os
import time
from collections.abc import Iterator
from contextlib import contextmanager, suppress
from pathlib import Path

History = dict[str, list[tuple[float, float]]]


class OutOfOrderSampleError(ValueError):
    """The sample is older than history already recorded for its currency."""


def open_entry(directory: int, name: str, flags: int) -> int:
    """Open a name inside the state directory without following a link."""
    # The state path is operator supplied. O_NOFOLLOW stops a link planted under
    # one of its names from redirecting the lock, the read, or the write.
    flags |= os.O_NOFOLLOW | os.O_CLOEXEC
    # macOS can report ENOENT to one of two openat(O_CREAT) calls that race to
    # create the same name, so a creating open gets a few attempts.
    attempts = 5 if flags & os.O_CREAT else 1
    while True:
        attempts -= 1
        try:
            return os.open(name, flags, 0o600, dir_fd=directory)
        except FileNotFoundError:
            if not attempts:
                raise
        except OSError as exc:
            # Linux and macOS report ELOOP; FreeBSD reports EMLINK.
            if exc.errno in (errno.ELOOP, errno.EMLINK):
                raise OSError(
                    f"State path must not be a symbolic link: {name}"
                ) from exc
            raise


def parse_history(content: bytes) -> History:
    """Return the stored samples, or nothing if any part of them is invalid."""
    try:
        raw = json.loads(content)
        if not isinstance(raw, dict):
            return {}
        history: History = {}
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
    except (ValueError, TypeError, OverflowError):
        return {}


def read_history(directory: int, name: str) -> History:
    try:
        descriptor = open_entry(directory, name, os.O_RDONLY)
    except FileNotFoundError:
        return {}
    with open(descriptor, "rb") as stream:
        return parse_history(stream.read())


def write_history(directory: int, name: str, history: History) -> None:
    temporary = f".{name}.tmp"
    # The caller holds the lock, so a file under this name is a leftover.
    with suppress(FileNotFoundError):
        os.unlink(temporary, dir_fd=directory)
    descriptor = open_entry(directory, temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    try:
        with open(descriptor, "w", encoding="utf-8") as stream:
            json.dump(history, stream, allow_nan=False, separators=(",", ":"))
        os.replace(temporary, name, src_dir_fd=directory, dst_dir_fd=directory)
    except BaseException:
        with suppress(FileNotFoundError):
            os.unlink(temporary, dir_fd=directory)
        raise


@contextmanager
def locked_directory(path: Path) -> Iterator[int]:
    """Hold the state directory open and its sibling lock file exclusively."""
    import fcntl

    # Every later operation is relative to this descriptor, so replacing an
    # ancestor of the state path after this point cannot redirect them.
    directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC)
    try:
        # Replacing the history changes its inode, so it cannot itself be the lock.
        descriptor = open_entry(
            directory, path.name + ".lock", os.O_WRONLY | os.O_CREAT | os.O_APPEND
        )
        with open(descriptor, "a") as lock:
            deadline = time.monotonic() + 1
            while True:
                try:
                    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except BlockingIOError:
                    if time.monotonic() >= deadline:
                        raise
                    time.sleep(0.01)
            yield directory
    finally:
        os.close(directory)


def record_price(
    path: Path, currency: str, window: float, timestamp: float, price: float
) -> tuple[float | None, float]:
    """Serialize the read/modify/replace cycle on a stable sibling lock file."""
    with locked_directory(path) as directory:
        history = read_history(directory, path.name)
        samples = dict(history.get(currency, []))
        # Retention is relative to the newest sample, so the baseline an older
        # sample needs may already be pruned. Refuse it rather than report a
        # missing baseline as pending.
        if samples and timestamp < max(samples):
            raise OutOfOrderSampleError("Quote is older than recorded history")
        samples[timestamp] = price
        newest = max(samples)
        ordered = sorted((t, p) for t, p in samples.items() if t >= newest - window)
        history[currency] = ordered
        write_history(directory, path.name, history)
        for start, baseline in ordered:
            if start < timestamp and baseline > 0:
                move = (price - baseline) / baseline * 100
                if not math.isfinite(move):
                    raise ValueError("Window movement cannot be represented")
                return move, timestamp - start
        return None, 0.0
