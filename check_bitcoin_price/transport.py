# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

"""HTTP retrieval with bounded retries and a total check deadline."""

import json
import math
import time
from email.utils import parsedate_to_datetime
from queue import Empty, Queue
from threading import Thread

import requests

MAX_RESPONSE_BYTES = 64 * 1024
RETRYABLE_STATUS = {408, 429, 500, 502, 503, 504}
TIMEOUT_MESSAGE = "Total timeout expired"


def retry_delay(response: requests.Response | None, attempt: int) -> float:
    """Honor Retry-After; otherwise use exponential backoff."""
    fallback: float = 0.5 * 2.0**attempt
    if response is None or "Retry-After" not in response.headers:
        return fallback
    value = response.headers["Retry-After"]
    try:
        seconds = float(value)
    except ValueError:
        try:
            seconds = parsedate_to_datetime(value).timestamp() - time.time()
        except (TypeError, ValueError, OverflowError):
            return fallback
    return max(0.0, seconds) if math.isfinite(seconds) else fallback


def close_redirect_body(response: requests.Response, **kwargs: object) -> None:
    # Requests otherwise buffers an entire redirect body before following Location.
    if response.is_redirect:
        response.close()


def fetch_with_retries(
    url: str, params: dict[str, str], deadline: float, retries: int
) -> object:
    """Retry only transient transport failures and selected HTTP statuses."""
    for attempt in range(retries + 1):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise requests.Timeout(TIMEOUT_MESSAGE)
        try:
            with requests.get(
                url,
                params=params,
                timeout=remaining,
                stream=True,
                hooks={"response": close_redirect_body},
                headers={"Accept": "application/json"},
            ) as response:
                if response.status_code not in RETRYABLE_STATUS or attempt == retries:
                    response.raise_for_status()
                    body = bytearray()
                    for chunk in response.iter_content(8192):
                        if time.monotonic() >= deadline:
                            raise requests.Timeout(TIMEOUT_MESSAGE)
                        if len(body) + len(chunk) > MAX_RESPONSE_BYTES:
                            raise ValueError("Quote response exceeds 64 KiB")
                        body.extend(chunk)
                    return json.loads(body)
                # Close the response before waiting or making another request.
                delay = retry_delay(response, attempt)
                if delay >= deadline - time.monotonic():
                    # Report the status that caused the wait, not a timeout.
                    response.raise_for_status()
        except (requests.Timeout, requests.ConnectionError):
            if attempt == retries:
                raise
            delay = retry_delay(None, attempt)
            if delay >= deadline - time.monotonic():
                raise
        time.sleep(delay)
    raise requests.Timeout(TIMEOUT_MESSAGE)  # pragma: no cover


def fetch_json(
    url: str, params: dict[str, str], timeout: float, retries: int
) -> object:
    """Bound DNS, connect, body reads, decoding, and retries by one deadline.

    Requests' timeout is an inactivity limit, not a wall-clock deadline. A daemon
    worker lets the CLI return UNKNOWN on time even if a peer slowly drips data.
    The worker owns and closes its response; it cannot print or submit more
    retries once its deadline expires. It does not block interpreter shutdown.
    """
    deadline = time.monotonic() + timeout
    results: Queue[object] = Queue(maxsize=1)

    def retrieve() -> None:
        try:
            results.put(fetch_with_retries(url, params, deadline, retries))
        except Exception as exc:
            results.put(exc)

    Thread(target=retrieve, daemon=True).start()
    try:
        result = results.get(timeout=max(0.0, deadline - time.monotonic()))
    except Empty as exc:
        raise requests.Timeout(TIMEOUT_MESSAGE) from exc
    if time.monotonic() >= deadline:
        raise requests.Timeout(TIMEOUT_MESSAGE)
    if isinstance(result, Exception):
        raise result
    return result
