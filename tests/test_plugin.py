"""Tests for the Bitcoin price checker Nagios plugin."""

import pytest
import responses

from check_bitcoin_price.plugin import (
    CRITICAL,
    DEFAULT_API_URL,
    OK,
    UNKNOWN,
    WARNING,
    BitcoinPriceChecker,
    main,
    parse_args,
    parse_range,
)


class TestBitcoinPriceChecker:
    """Tests for BitcoinPriceChecker class."""

    @responses.activate
    def test_get_bitcoin_price_success(self):
        """Test successful price fetch."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 43521.50}},
            status=200,
        )

        checker = BitcoinPriceChecker()
        price = checker.get_bitcoin_price()

        assert price == 43521.50

    @responses.activate
    def test_get_bitcoin_price_different_currency(self):
        """Test price fetch in different currency."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"eur": 40000.00}},
            status=200,
        )

        checker = BitcoinPriceChecker(currency="eur")
        price = checker.get_bitcoin_price()

        assert price == 40000.00

    @responses.activate
    def test_get_bitcoin_price_api_error(self):
        """Test API error handling."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"error": "rate limit exceeded"},
            status=429,
        )

        checker = BitcoinPriceChecker()

        with pytest.raises(Exception):
            checker.get_bitcoin_price()

    def test_check_thresholds_ok(self):
        """Test OK status when price is within thresholds."""
        checker = BitcoinPriceChecker()
        result = checker.check_thresholds(
            price=40000,
            warning_low=30000,
            warning_high=50000,
            critical_low=25000,
            critical_high=60000,
        )

        assert result.status == OK
        assert "OK" in result.message
        assert "40000.00" in result.message

    def test_check_thresholds_warning_low(self):
        """Test WARNING status when price is below warning threshold."""
        checker = BitcoinPriceChecker()
        result = checker.check_thresholds(
            price=28000,
            warning_low=30000,
            warning_high=50000,
            critical_low=25000,
            critical_high=60000,
        )

        assert result.status == WARNING
        assert "WARNING" in result.message
        assert "below" in result.message

    def test_check_thresholds_warning_high(self):
        """Test WARNING status when price is above warning threshold."""
        checker = BitcoinPriceChecker()
        result = checker.check_thresholds(
            price=55000,
            warning_low=30000,
            warning_high=50000,
            critical_low=25000,
            critical_high=60000,
        )

        assert result.status == WARNING
        assert "WARNING" in result.message
        assert "above" in result.message

    def test_check_thresholds_critical_low(self):
        """Test CRITICAL status when price is below critical threshold."""
        checker = BitcoinPriceChecker()
        result = checker.check_thresholds(
            price=20000,
            warning_low=30000,
            warning_high=50000,
            critical_low=25000,
            critical_high=60000,
        )

        assert result.status == CRITICAL
        assert "CRITICAL" in result.message
        assert "below" in result.message

    def test_check_thresholds_critical_high(self):
        """Test CRITICAL status when price is above critical threshold."""
        checker = BitcoinPriceChecker()
        result = checker.check_thresholds(
            price=65000,
            warning_low=30000,
            warning_high=50000,
            critical_low=25000,
            critical_high=60000,
        )

        assert result.status == CRITICAL
        assert "CRITICAL" in result.message
        assert "above" in result.message

    def test_check_thresholds_no_thresholds(self):
        """Test OK status when no thresholds are set."""
        checker = BitcoinPriceChecker()
        result = checker.check_thresholds(price=100000)

        assert result.status == OK

    def test_check_thresholds_partial_thresholds(self):
        """Test with only some thresholds set."""
        checker = BitcoinPriceChecker()

        # Only low thresholds
        result = checker.check_thresholds(
            price=20000,
            critical_low=25000,
        )
        assert result.status == CRITICAL

        # Only high thresholds
        result = checker.check_thresholds(
            price=100000,
            warning_high=50000,
        )
        assert result.status == WARNING


class TestParseArgs:
    """Tests for argument parsing."""

    def test_parse_args_defaults(self):
        """Test default argument values."""
        args = parse_args([])

        assert args.warning is None
        assert args.critical is None
        assert args.currency == "usd"
        assert args.timeout == 10
        assert args.verbose is False

    def test_parse_args_warning_critical(self):
        """Test parsing warning and critical thresholds."""
        args = parse_args(["-w", "30000:50000", "-c", "25000:60000"])

        assert args.warning == "30000:50000"
        assert args.critical == "25000:60000"

    def test_parse_args_individual_thresholds(self):
        """Test parsing individual threshold arguments."""
        args = parse_args(
            [
                "--warning-low",
                "30000",
                "--warning-high",
                "50000",
                "--critical-low",
                "25000",
                "--critical-high",
                "60000",
            ]
        )

        assert args.warning_low == 30000
        assert args.warning_high == 50000
        assert args.critical_low == 25000
        assert args.critical_high == 60000

    def test_parse_args_currency(self):
        """Test parsing currency argument."""
        args = parse_args(["--currency", "eur"])

        assert args.currency == "eur"

    def test_parse_args_timeout(self):
        """Test parsing timeout argument."""
        args = parse_args(["--timeout", "30"])

        assert args.timeout == 30

    def test_parse_args_verbose(self):
        """Test parsing verbose flag."""
        args = parse_args(["-v"])

        assert args.verbose is True


class TestParseRange:
    """Tests for range parsing."""

    def test_parse_range_full(self):
        """Test parsing full range."""
        low, high = parse_range("30000:50000")

        assert low == 30000
        assert high == 50000

    def test_parse_range_low_only(self):
        """Test parsing range with only low value."""
        low, high = parse_range("30000:")

        assert low == 30000
        assert high is None

    def test_parse_range_high_only(self):
        """Test parsing range with only high value."""
        low, high = parse_range(":50000")

        assert low is None
        assert high == 50000

    def test_parse_range_invalid_no_colon(self):
        """Test parsing invalid range without colon."""
        with pytest.raises(ValueError):
            parse_range("30000")

    def test_parse_range_invalid_multiple_colons(self):
        """Test parsing invalid range with multiple colons."""
        with pytest.raises(ValueError):
            parse_range("30000:40000:50000")


class TestMain:
    """Tests for main function."""

    @responses.activate
    def test_main_ok(self, capsys):
        """Test main function returns OK."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 40000}},
            status=200,
        )

        exit_code = main([])

        assert exit_code == OK
        captured = capsys.readouterr()
        assert "OK" in captured.out
        assert "bitcoin_price=" in captured.out

    @responses.activate
    def test_main_warning(self, capsys):
        """Test main function returns WARNING."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 28000}},
            status=200,
        )

        exit_code = main(["--warning-low", "30000"])

        assert exit_code == WARNING
        captured = capsys.readouterr()
        assert "WARNING" in captured.out

    @responses.activate
    def test_main_critical(self, capsys):
        """Test main function returns CRITICAL."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 20000}},
            status=200,
        )

        exit_code = main(["--critical-low", "25000"])

        assert exit_code == CRITICAL
        captured = capsys.readouterr()
        assert "CRITICAL" in captured.out

    @responses.activate
    def test_main_api_error(self, capsys):
        """Test main function returns UNKNOWN on API error."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"error": "server error"},
            status=500,
        )

        exit_code = main([])

        assert exit_code == UNKNOWN
        captured = capsys.readouterr()
        assert "UNKNOWN" in captured.out

    @responses.activate
    def test_main_with_range_thresholds(self, capsys):
        """Test main function with range-style thresholds."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 55000}},
            status=200,
        )

        exit_code = main(["-w", "30000:50000", "-c", "25000:60000"])

        assert exit_code == WARNING
        captured = capsys.readouterr()
        assert "WARNING" in captured.out
        assert "above" in captured.out

    @responses.activate
    def test_main_performance_data(self, capsys):
        """Test that performance data is included in output."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 43521.50}},
            status=200,
        )

        main([])

        captured = capsys.readouterr()
        assert "| bitcoin_price=43521.50" in captured.out


class TestEdgeCases:
    """Tests for edge cases."""

    @responses.activate
    def test_zero_price(self):
        """Test handling of zero price."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 0}},
            status=200,
        )

        checker = BitcoinPriceChecker()
        price = checker.get_bitcoin_price()

        assert price == 0

    @responses.activate
    def test_very_large_price(self):
        """Test handling of very large price."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 1000000000}},
            status=200,
        )

        checker = BitcoinPriceChecker()
        price = checker.get_bitcoin_price()

        assert price == 1000000000

    @responses.activate
    def test_decimal_price(self):
        """Test handling of price with many decimal places."""
        responses.add(
            responses.GET,
            DEFAULT_API_URL,
            json={"bitcoin": {"usd": 43521.123456789}},
            status=200,
        )

        checker = BitcoinPriceChecker()
        price = checker.get_bitcoin_price()

        assert price == pytest.approx(43521.123456789)

    def test_threshold_at_boundary(self):
        """Test price exactly at threshold boundary."""
        checker = BitcoinPriceChecker()

        # Price exactly at warning_low should not trigger warning
        result = checker.check_thresholds(
            price=30000,
            warning_low=30000,
        )
        assert result.status == OK

        # Price exactly at warning_high should not trigger warning
        result = checker.check_thresholds(
            price=50000,
            warning_high=50000,
        )
        assert result.status == OK

    def test_currency_case_insensitive(self):
        """Test that currency is case insensitive."""
        checker_lower = BitcoinPriceChecker(currency="usd")
        checker_upper = BitcoinPriceChecker(currency="USD")
        checker_mixed = BitcoinPriceChecker(currency="Usd")

        assert checker_lower.currency == "usd"
        assert checker_upper.currency == "usd"
        assert checker_mixed.currency == "usd"
