"""Build architecture-independent Linux packages and release checksums."""

import hashlib
import os
import shutil

# Commands below use resolved executable paths, fixed arguments, and no shell.
import subprocess  # nosec B404
from pathlib import Path

from check_bitcoin_price import __version__


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    distribution = root / "dist"
    distribution.mkdir(exist_ok=True)
    nfpm = shutil.which("nfpm")
    git = shutil.which("git")
    if nfpm is None or git is None:
        raise RuntimeError("nfpm and git are required; run mise install")
    environment = {**os.environ, "PACKAGE_VERSION": __version__}
    environment.setdefault(
        "SOURCE_DATE_EPOCH",
        subprocess.check_output(  # nosec B603
            [git, "log", "-1", "--format=%ct"], cwd=root, text=True
        ).strip(),
    )
    for package_format in ("deb", "rpm"):
        subprocess.run(  # nosec B603
            [
                nfpm,
                "package",
                "--config",
                "packaging/nfpm.yaml",
                "--packager",
                package_format,
                "--target",
                str(distribution),
            ],
            cwd=root,
            env=environment,
            check=True,
        )
    artifacts = sorted(
        path
        for path in distribution.iterdir()
        if path.name.endswith((".deb", ".rpm", ".whl", ".tar.gz"))
    )
    checksum_lines = [
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
        for path in artifacts
    ]
    (distribution / "SHA256SUMS").write_text("".join(checksum_lines))


if __name__ == "__main__":
    main()
