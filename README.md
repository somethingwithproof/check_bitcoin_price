# check_bitcoin_price

A Nagios/Icinga plugin to monitor Bitcoin price with configurable warning and critical thresholds.

[![Python Version](https://img.shields.io/pypi/pyversions/check-bitcoin-price.svg)](https://pypi.org/project/check-bitcoin-price/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)

## Features

- Monitor Bitcoin price in multiple currencies (USD, EUR, GBP, etc.)
- Configurable warning and critical thresholds (high and low)
- Standard Nagios plugin output with performance data
- Uses CoinGecko API (free, no API key required)
- Support for custom API endpoints
- Configurable timeout
- Quote freshness checks using vendor timestamps
- Bounded retries for rate limits and temporary API failures
- Optional alerts on absolute 24-hour percentage movement
- Price thresholds, request duration, and quote age in performance data

## Installation

### From PyPI

```bash
pip install check-bitcoin-price
```

### From Source

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### For Development

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Usage

### Basic Usage

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### With Thresholds

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Individual Thresholds

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Different Currency

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Custom Timeout

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Freshness and Retry Budget

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Freshness is opt-in for compatibility with custom endpoints that return only a
price. With `--max-age`, missing, invalid, future, or stale vendor timestamps
return `UNKNOWN`; the plugin does not substitute the local fetch time for the
vendor's quote time. A timestamp exactly at the age limit remains acceptable.

The default allows one retry. Only connection errors, timeouts, and HTTP
408/429/500/502/503/504 responses are retried. Backoff starts at 0.5 seconds and
doubles for subsequent retries; `Retry-After` seconds and HTTP dates take
precedence. All attempts, response reads, JSON decoding, and retry waits share
the `--timeout` budget. A retry wait that cannot fit returns `UNKNOWN` immediately.
Authentication failures, other permanent HTTP errors, and invalid JSON are not
retried. Use `--retries 0` to disable retries.

### Daily Percentage Movement

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Change thresholds measure the absolute value of CoinGecko's signed 24-hour
percentage change in the selected currency. A change exactly at a threshold does
not alert. If both thresholds are supplied, warning must not exceed critical.
Missing or invalid required change data returns `UNKNOWN`. Price and change
alerts can be combined; the highest severity wins, with price taking precedence
when severities match.

## Command Line Options

| Option | Description |
|--------|-------------|
| `-w`, `--warning` | Warning threshold range (format: LOW:HIGH) |
| `-c`, `--critical` | Critical threshold range (format: LOW:HIGH) |
| `--warning-low` | Warning threshold for low price |
| `--warning-high` | Warning threshold for high price |
| `--critical-low` | Critical threshold for low price |
| `--critical-high` | Critical threshold for high price |
| `--currency` | Currency to check price in (default: usd) |
| `--timeout` | Total API request/retry budget in seconds, including fractional values (default: 10) |
| `--retries` | Additional transient attempts, 0–5 (default: 1) |
| `--max-age` | Maximum vendor quote age in seconds; disabled by default |
| `--warning-change` | Warning limit for absolute 24-hour percentage movement |
| `--critical-change` | Critical limit for absolute 24-hour percentage movement |
| `--api-url` | Custom API URL |
| `-v`, `--verbose` | Enable verbose output |
| `-V`, `--version` | Show version |
| `-h`, `--help` | Show help message |

## Nagios Configuration

### Command Definition

Add to your Nagios commands configuration:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    /usr/local/bin/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Service Definition

```cfg
define service {
    use                     generic-service
    host_name               localhost
    service_description     Bitcoin Price
    check_command           check_bitcoin_price!30000:50000!25000:60000!usd
    check_interval          15
    retry_interval          5
}
```

### Icinga2 Configuration

```conf
object CheckCommand "bitcoin_price" {
    command = [ PluginDir + "/check_bitcoin_price" ]

    arguments = {
        "-w" = "$bitcoin_warning$"
        "-c" = "$bitcoin_critical$"
        "--currency" = "$bitcoin_currency$"
    }
}

object Service "bitcoin-price" {
    import "generic-service"
    host_name = NodeName
    check_command = "bitcoin_price"

    vars.bitcoin_warning = "30000:50000"
    vars.bitcoin_critical = "25000:60000"
    vars.bitcoin_currency = "usd"
}
```

## Exit Codes

Invalid arguments, nonpositive timeouts, invalid threshold ranges, and malformed
API prices return `UNKNOWN` (exit 3). Thresholds must be finite, nonnegative
numbers, with each low bound no greater than its high bound. Invalid configuration
is rejected before contacting the API. Prices must be finite and nonnegative;
invalid responses do not emit performance data. Verbose diagnostics go to stderr
so stdout contains a single monitoring status line.

| Code | Status | Description |
|------|--------|-------------|
| 0 | OK | Price is within acceptable range |
| 1 | WARNING | Price crossed warning threshold |
| 2 | CRITICAL | Price crossed critical threshold |
| 3 | UNKNOWN | Error occurred (API failure, timeout, etc.) |

## Performance Data

The plugin outputs performance data in standard Nagios format:

```
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Price performance data now includes the configured warning/critical ranges and
a minimum of zero. Request time includes all attempts and backoff. Quote age is
emitted only when the vendor supplies a valid timestamp; daily change is emitted
when available. Change ranges are symmetric around zero. Invalid or stale data
produces `UNKNOWN` without price performance data. These metrics can be used with
graphing tools like PNP4Nagios, Grafana, or InfluxDB.

## API

This plugin uses the [CoinGecko API](https://www.coingecko.com/en/api) by default, which is free and doesn't require an API key. Rate limits apply.

Custom endpoints must use the same response shape: `bitcoin.<currency>` for
price, `bitcoin.last_updated_at` for UNIX timestamp seconds, and
`bitcoin.<currency>_24h_change` for signed daily percentage movement. Only price
is required when freshness and movement alerts are disabled.

Supported currencies include: usd, eur, gbp, jpy, aud, cad, chf, cny, and many more.

## Development

Install [mise](https://mise.jdx.dev/getting-started.html), then run the development setup above. `mise.toml` pins Python and uv. Development tools are declared in `pyproject.toml` and resolved in the committed `uv.lock`.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run format
```

Install the commit hooks after setup:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Use `mise exec -- uv add --dev <tool>` or `mise exec -- uv add <dependency>` to update dependencies and commit both `pyproject.toml` and `uv.lock`.

CI checks Python 3.12 and 3.13 on Linux and Python 3.13 on macOS. Every PR also runs package validation, dependency auditing, and CodeQL. Built distributions are available as the `distributions` artifact on CI runs.

The package and CLI version comes from `check_bitcoin_price/__init__.py`. Update that value before a release and build with `mise run build`. Distribution uploads are a separate release step.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow and signed-off commit requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Thomas Vincent

## Acknowledgments

- [CoinGecko](https://www.coingecko.com/) for providing a free cryptocurrency API
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
