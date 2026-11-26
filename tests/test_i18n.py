# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

"""Tests for 20-locale i18n support in check_bitcoin_price."""

import re

import pytest

from check_bitcoin_price.i18n import (
    DEFAULT_LOCALE,
    SUPPORTED_LOCALES,
    detect_locale,
    get_locale,
    load_catalog,
    normalize_locale,
    set_locale,
    t,
)
from check_bitcoin_price.plugin import BitcoinPriceChecker, parse_args

PLACEHOLDER_RE = re.compile(r"\{[a-zA-Z0-9_]+\}|%\([a-zA-Z0-9_]+\)s")
NAGIOS_PREFIXES = ("OK - ", "WARNING - ", "CRITICAL - ", "UNKNOWN - ")


@pytest.fixture(autouse=True)
def _reset_locale(monkeypatch: pytest.MonkeyPatch) -> None:
    for var in ("LC_ALL", "LC_MESSAGES", "LANG"):
        monkeypatch.delenv(var, raising=False)
    set_locale(None)
    yield
    set_locale(None)


def test_all_20_locales_load_with_key_placeholder_and_prefix_parity() -> None:
    assert len(SUPPORTED_LOCALES) == 20
    en = load_catalog(DEFAULT_LOCALE)
    assert len(en) > 0
    for locale in SUPPORTED_LOCALES:
        catalog = load_catalog(locale)
        assert set(catalog.keys()) == set(en.keys()), locale
        for key, en_val in en.items():
            val = catalog[key]
            assert val.strip(), (locale, key)
            assert sorted(PLACEHOLDER_RE.findall(val)) == sorted(
                PLACEHOLDER_RE.findall(en_val)
            ), (locale, key)
            for prefix in NAGIOS_PREFIXES:
                if en_val.startswith(prefix):
                    assert val.startswith(prefix), (locale, key)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (None, "en"),
        ("", "en"),
        ("   ", "en"),
        ("C", "en"),
        ("POSIX", "en"),
        ("C.UTF-8", "en"),
        ("de_DE.UTF-8", "de"),
        ("de_AT@euro", "de"),
        ("zh_TW", "zh-TW"),
        ("zh_HK.UTF-8", "zh-TW"),
        ("zh-Hant-TW", "zh-TW"),
        ("zh_CN.UTF-8", "zh-CN"),
        ("zh", "zh-CN"),
        ("pt_BR.UTF-8", "pt-BR"),
        ("pt_PT", "pt-BR"),
        ("hi_IN.UTF-8", "hi"),
        ("xx_YY", "en"),
    ],
)
def test_normalize_locale(raw: str | None, expected: str) -> None:
    assert normalize_locale(raw) == expected


def test_env_precedence_and_override(monkeypatch: pytest.MonkeyPatch) -> None:
    assert detect_locale() == "en"
    monkeypatch.setenv("LANG", "es_ES.UTF-8")
    assert detect_locale() == "es"
    monkeypatch.setenv("LC_MESSAGES", "ja_JP.UTF-8")
    assert detect_locale() == "ja"
    monkeypatch.setenv("LC_ALL", "fr_FR.UTF-8")
    assert detect_locale() == "fr"
    assert detect_locale("de") == "de"

    assert set_locale("ko") == "ko"
    assert get_locale() == "ko"
    assert set_locale(None) == "fr"
    assert get_locale() == "fr"


def test_translation_fallback_and_cli_lang(capsys: pytest.CaptureFixture[str]) -> None:
    assert t("missing.key.fallback") == "missing.key.fallback"
    assert t("missing.key.fallback", locale="de") == "missing.key.fallback"
    assert t("status.price_ok", price="40000.00", currency="USD") == (
        "OK - Bitcoin price is 40000.00 USD"
    )

    parsed = parse_args(["--lang", "de"])
    assert parsed.lang == "de"
    assert get_locale() == "de"

    result = BitcoinPriceChecker().check_thresholds(price=40000)
    assert result.message.startswith("OK - ")
    assert result.message == t(
        "status.price_ok", locale="de", price="40000.00", currency="USD"
    )

    parsed_eq = parse_args(["--lang=ja"])
    assert parsed_eq.lang == "ja"
    assert get_locale() == "ja"

    with pytest.raises(SystemExit) as exc:
        parse_args(["--lang=fr", "--help"])
    assert exc.value.code == 0
    assert t("cli.description", locale="fr") in capsys.readouterr().out
