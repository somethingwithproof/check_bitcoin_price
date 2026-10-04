"""Release validation must reject ambiguous versions and mismatched artifacts."""

import pytest

from scripts.validate_release import validate_tag


@pytest.mark.parametrize("version", ["0.0.0", "1.0.0", "12.34.56"])
def test_stable_semver(version: str) -> None:
    assert validate_tag(f"v{version}", version) == f"v{version}"


@pytest.mark.parametrize(
    "tag",
    [
        "1.0.0",
        "v1.0",
        "v01.0.0",
        "v1.00.0",
        "v1.0.00",
        "v1.0.0-beta.1",
        "v1.0.0+build.1",
        "v1.0.0\n",
        "v1٢.0.0",
        "main",
        "",
    ],
)
def test_invalid_release_tag(tag: str) -> None:
    with pytest.raises(ValueError, match="stable SemVer"):
        validate_tag(tag)


def test_tag_must_match_package_version() -> None:
    with pytest.raises(ValueError, match="must match"):
        validate_tag("v2.0.0", "1.0.0")
