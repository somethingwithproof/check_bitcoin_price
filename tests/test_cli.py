"""Test the installed wheel's console command against a local HTTP server."""

import json
import os
import subprocess
import sysconfig
import time
import venv
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlsplit

import hatchling.build
import pytest


@pytest.fixture(scope="session")
def installed_cli(tmp_path_factory):
    root = tmp_path_factory.mktemp("installed-cli")
    wheel = root / hatchling.build.build_wheel(str(root))
    environment = root / "venv"
    venv.EnvBuilder(with_pip=False, symlinks=os.name != "nt").create(environment)
    scripts = environment / ("Scripts" if os.name == "nt" else "bin")
    python = scripts / ("python.exe" if os.name == "nt" else "python")
    site = subprocess.run(
        [str(python), "-c", "import sysconfig; print(sysconfig.get_path('purelib'))"],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    # Reuse only test-runner dependencies; the project itself comes from its wheel.
    (Path(site) / "test_dependencies.pth").write_text(
        sysconfig.get_path("purelib") + "\n"
    )
    subprocess.run(
        [
            "uv",
            "pip",
            "install",
            "--python",
            str(python),
            "--no-index",
            "--no-deps",
            "--no-build",
            str(wheel),
        ],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    origin = subprocess.run(
        [
            str(python),
            "-c",
            "import check_bitcoin_price; print(check_bitcoin_price.__file__)",
        ],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    assert Path(origin).is_relative_to(environment)
    command = scripts / (
        "check_bitcoin_price.exe" if os.name == "nt" else "check_bitcoin_price"
    )
    return command, root


@pytest.fixture
def api_server():
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, message_format, *args):
            pass

        def do_GET(self):
            path = urlsplit(self.path).path
            price = {"/warning": 28000, "/critical": 20000}.get(path, 40000)
            quote = {"usd": price, "usd_24h_change": -6}
            if path != "/missing":
                quote["last_updated_at"] = int(time.time()) - (
                    600 if path == "/stale" else 0
                )
            body = json.dumps({"bitcoin": quote}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            try:
                if path == "/slow":
                    for byte in body:
                        self.wfile.write(bytes([byte]))
                        self.wfile.flush()
                        time.sleep(0.02)
                else:
                    self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError):
                pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(
        target=server.serve_forever, kwargs={"poll_interval": 0.01}, daemon=True
    )
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=1)


@pytest.mark.parametrize(
    "path, extra, expected",
    [
        ("/ok", [], 0),
        ("/warning", ["--warning-low", "30000"], 1),
        ("/critical", ["--critical-low", "25000"], 2),
        ("/stale", ["--max-age", "300"], 3),
        ("/missing", ["--max-age", "300"], 3),
        ("/ok", ["--warning-change", "5"], 1),
        ("/ok", ["--timeout", "0"], 3),
    ],
)
def test_installed_command_exit_codes(installed_cli, api_server, path, extra, expected):
    command, cwd = installed_cli
    result = subprocess.run(
        [str(command), "--api-url", api_server + path, *extra],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=5,
    )
    assert result.returncode == expected
    assert len(result.stdout.splitlines()) == 1
    assert result.stdout.startswith(("OK", "WARNING", "CRITICAL", "UNKNOWN")[expected])
    if expected == 3:
        assert "bitcoin_price=" not in result.stdout


def test_slow_drip_cannot_extend_total_deadline(installed_cli, api_server):
    command, cwd = installed_cli
    started = time.monotonic()
    result = subprocess.run(
        [
            str(command),
            "--api-url",
            api_server + "/slow",
            "--timeout",
            "0.2",
            "--retries",
            "0",
        ],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=3,
    )
    assert result.returncode == 3
    assert "timed out" in result.stdout
    # Includes interpreter startup. The response would take over 2 seconds to drip.
    assert time.monotonic() - started < 1.5
