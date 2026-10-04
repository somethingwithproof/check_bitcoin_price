"""HTTP retrieval with bounded retries and a total check deadline."""

import math
import time
from email.utils import parsedate_to_datetime
from queue import Empty, Queue
from threading import Thread

import requests

RETRYABLE_STATUS = {408, 429, 500, 502, 503, 504}


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


def fetch_with_retries(
    url: str, params: dict[str, str], deadline: float, retries: int
) -> object:
    """Retry only transient transport failures and selected HTTP statuses."""
    for attempt in range(retries + 1):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise requests.Timeout("Total timeout expired")
        try:
            with requests.get(
                url,
                params=params,
                timeout=remaining,
                headers={"Accept": "application/json"},
            ) as response:
                if response.status_code not in RETRYABLE_STATUS or attempt == retries:
                    response.raise_for_status()
                    return response.json()
                # Close the response before waiting or making another request.
                delay = retry_delay(response, attempt)
        except (requests.Timeout, requests.ConnectionError):
            if attempt == retries:
                raise
            delay = retry_delay(None, attempt)
        if delay >= deadline - time.monotonic():
            raise requests.Timeout("Retry delay exceeds the total timeout")
        time.sleep(delay)
    raise requests.Timeout("Total timeout expired")  # pragma: no cover


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
        raise requests.Timeout("Total timeout expired") from exc
    if time.monotonic() >= deadline:
        raise requests.Timeout("Total timeout expired")
    if isinstance(result, Exception):
        raise result
    return result
