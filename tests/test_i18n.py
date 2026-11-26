# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

"""Tests for 48-locale i18n support in check_bitcoin_price."""

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


def test_all_48_locales_load_with_key_placeholder_and_prefix_parity() -> None:
    assert len(SUPPORTED_LOCALES) == 48
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
        ("zh-TW-x-demo", "zh-TW"),
        ("zh-HK-x-demo", "zh-TW"),
        ("zh-Hant-TW", "zh-TW"),
        ("zh-Hans-TW", "zh-CN"),
        ("zh_CN.UTF-8", "zh-CN"),
        ("zh", "zh-CN"),
        ("pt_BR.UTF-8", "pt-BR"),
        ("pt_PT", "pt-BR"),
        ("hi_IN.UTF-8", "hi"),
        ("x-demo", "en"),
        ("ar_EG.UTF-8", "ar-EG"),
        ("ar-MA-u-nu-latn", "ar-MA"),
        ("ar-Arab-EG", "ar-EG"),
        ("ar-Arab-SA", "ar"),
        ("fr_MA.UTF-8", "fr-MA"),
        ("fr-SN-x-test", "fr-SN"),
        ("fr_CA.UTF-8", "fr"),
        ("af", "af-ZA"),
        ("am_ET.UTF-8", "am-ET"),
        ("ha", "ha-NG"),
        ("ig", "ig-NG"),
        ("mg", "mg-MG"),
        ("rw", "rw-RW"),
        ("so", "so-SO"),
        ("sw_KE.UTF-8", "sw-KE"),
        ("xh", "xh-ZA"),
        ("yo", "yo-NG"),
        ("zu", "zu-ZA"),
        ("bn_BD.UTF-8", "bn"),
        ("fa_IR", "fa"),
        ("iw", "he"),
        ("mr_IN", "mr"),
        ("ta_IN", "ta"),
        ("te_IN", "te"),
        ("th_TH", "th"),
        ("ur_PK", "ur"),
        ("ms_MY.UTF-8", "ms"),
        ("tl_PH.UTF-8", "fil"),
        ("bs", "bs"),
        ("bs-BA", "bs"),
        ("bs_BA.UTF-8", "bs"),
        ("hr", "hr"),
        ("hr-HR", "hr"),
        ("hr_HR.UTF-8", "hr"),
        ("sr", "sr"),
        ("sr-RS", "sr"),
        ("sr_RS.UTF-8", "sr"),
        ("sr-Cyrl", "sr"),
        ("sr-Latn", "sr"),
        ("sr-Cyrl-RS", "sr"),
        ("sr-Latn-RS", "sr"),
        ("sr_RS.UTF-8@latin", "sr"),
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

    for locale in SUPPORTED_LOCALES:
        with pytest.raises(SystemExit) as exc:
            parse_args([f"--lang={locale}", "--help"])
        assert exc.value.code == 0, locale
        out = capsys.readouterr().out
        assert " ".join(t("cli.description", locale=locale).split()) in " ".join(
            out.split()
        ), locale


def test_bcms_locales_script_distinction_and_lang_env_help(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    bs_cat = load_catalog("bs")
    hr_cat = load_catalog("hr")
    sr_cat = load_catalog("sr")

    # Serbian catalog must use Serbian Cyrillic script
    cyrillic_re = re.compile(r"[\u0400-\u04FF]")
    for key, val in sr_cat.items():
        assert cyrillic_re.search(val), key

    # Bosnian and Croatian catalogs must be genuinely distinct
    differing_keys = [k for k in bs_cat if bs_cat[k] != hr_cat[k]]
    assert len(differing_keys) >= 15
    assert bs_cat["cli.state_file_help"] != hr_cat["cli.state_file_help"]
    assert bs_cat["error.unexpected"] != hr_cat["error.unexpected"]
    assert bs_cat["cli.verbose_help"] != hr_cat["cli.verbose_help"]

    # Verify CLI --help renders cleanly via LANG environment variable
    for env_lang, expected_locale in (
        ("bs_BA.UTF-8", "bs"),
        ("hr_HR.UTF-8", "hr"),
        ("sr_RS.UTF-8", "sr"),
    ):
        monkeypatch.setenv("LANG", env_lang)
        set_locale(None)
        with pytest.raises(SystemExit) as exc:
            parse_args(["--help"])
        assert exc.value.code == 0, env_lang
        out = capsys.readouterr().out
        assert " ".join(
            t("cli.description", locale=expected_locale).split()
        ) in " ".join(out.split()), env_lang
