"""Validate stable SemVer tags against the package's single version source."""

import os
import re

from check_bitcoin_price import __version__

STABLE_TAG = re.compile(r"v(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", re.ASCII)


def validate_tag(tag: str, package_version: str = __version__) -> str:
    if STABLE_TAG.fullmatch(tag) is None:
        raise ValueError("Release tags must be stable SemVer: vMAJOR.MINOR.PATCH")
    if tag != f"v{package_version}":
        raise ValueError("Release tag must match check_bitcoin_price.__version__")
    return tag


if __name__ == "__main__":
    print(validate_tag(os.environ["RELEASE_TAG"]))
