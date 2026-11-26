# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** **English** · [Deutsch](docs/i18n/de/README.md) · [Español](docs/i18n/es/README.md) · [Français](docs/i18n/fr/README.md) · [Italiano](docs/i18n/it/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Nederlands](docs/i18n/nl/README.md) · [Русский](docs/i18n/ru/README.md) · [Українська](docs/i18n/uk/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [繁體中文](docs/i18n/zh-TW/README.md) · [العربية](docs/i18n/ar/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [Polski](docs/i18n/pl/README.md) · [Türkçe](docs/i18n/tr/README.md) · [Svenska](docs/i18n/sv/README.md) · [Tiếng Việt](docs/i18n/vi/README.md) · [Bahasa Indonesia](docs/i18n/id/README.md)

<details><summary>More languages (28 locales)</summary>

[Afrikaans](docs/i18n/af-ZA/README.md) · [አማርኛ](docs/i18n/am-ET/README.md) · [العربية (مصر)](docs/i18n/ar-EG/README.md) · [العربية (المغرب)](docs/i18n/ar-MA/README.md) · [বাংলা](docs/i18n/bn/README.md) · [Bosanski](docs/i18n/bs/README.md) · [فارسی](docs/i18n/fa/README.md) · [Filipino](docs/i18n/fil/README.md) · [Français (Maroc)](docs/i18n/fr-MA/README.md) · [Français (Sénégal)](docs/i18n/fr-SN/README.md) · [Hausa](docs/i18n/ha-NG/README.md) · [עברית](docs/i18n/he/README.md) · [Hrvatski](docs/i18n/hr/README.md) · [Igbo](docs/i18n/ig-NG/README.md) · [Malagasy](docs/i18n/mg-MG/README.md) · [मराठी](docs/i18n/mr/README.md) · [Bahasa Melayu](docs/i18n/ms/README.md) · [Kinyarwanda](docs/i18n/rw-RW/README.md) · [Soomaali](docs/i18n/so-SO/README.md) · [Српски](docs/i18n/sr/README.md) · [Kiswahili](docs/i18n/sw-KE/README.md) · [தமிழ்](docs/i18n/ta/README.md) · [తెలుగు](docs/i18n/te/README.md) · [ไทย](docs/i18n/th/README.md) · [اردو](docs/i18n/ur/README.md) · [isiXhosa](docs/i18n/xh-ZA/README.md) · [Yorùbá](docs/i18n/yo-NG/README.md) · [isiZulu](docs/i18n/zu-ZA/README.md)

</details>

A Nagios/Icinga plugin to monitor Bitcoin price with configurable warning and critical thresholds.

## Features

- Monitor Bitcoin price in multiple currencies (USD, EUR, GBP, etc.)
- Configurable warning and critical thresholds (high and low)
- Standard Nagios plugin output with performance data
- Uses CoinGecko API (free, no API key required)
- Support for custom API endpoints
- Configurable timeout
- Quote freshness checks using vendor timestamps, with a one-hour default limit
- Bounded retries for rate limits and temporary API failures
- One deadline for all attempts and a 64 KiB cap on each response
- Optional alerts on absolute 24-hour percentage movement
- Price thresholds, request duration, and quote age in performance data

## Installation

### From GitHub Releases

Download `.deb`, `.rpm`, `.tar.gz`, wheel, and `SHA256SUMS` files from [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Verify a download with `sha256sum --ignore-missing --check SHA256SUMS`. Releases after 1.0.0 also carry signed build provenance; confirm an asset came from this repository's release workflow with `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Use the filenames from the selected release. Native packages install `/usr/bin/check_bitcoin_price` and `/usr/lib/nagios/plugins/check_bitcoin_price`; the RPM also provides `/usr/lib64/nagios/plugins/check_bitcoin_price`. The packaged command runs Python in isolated mode, so it ignores `PYTHONPATH` and modules in the working directory; the system package manager resolves Python and `requests` dependencies. They contain architecture-independent Python code and require a distribution providing Python 3.12 or newer.

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

A quote that carries a vendor timestamp must be at most one hour old by default.
Endpoints that return only a price remain usable when `--max-age` is absent.
With `--max-age`, missing, invalid, future, or stale vendor timestamps return
`UNKNOWN`; the plugin does not substitute the local fetch time for the vendor's
quote time. A timestamp exactly at the age limit remains acceptable. Future
timestamps are always rejected.

The default allows one retry. Only connection errors, timeouts, and HTTP
408/429/500/502/503/504 responses are retried. Backoff starts at 0.5 seconds and
doubles for subsequent retries; `Retry-After` seconds and HTTP dates take
precedence. All attempts, response reads, JSON decoding, and retry waits share
the `--timeout` budget. A retry wait that cannot fit returns `UNKNOWN` immediately
and reports the failure that prompted it, such as `HTTP 429` or `ConnectionError`,
not a timeout. Authentication failures, other permanent HTTP errors, invalid
JSON, and responses larger than 64 KiB of decoded data are not retried. Use
`--retries 0` to disable retries.

### Fallback quote sources

Use repeatable `--fallback-url URL` options with CoinGecko-compatible endpoints.
For example, add `--fallback-url https://quotes.example.org/simple/price`.
Each source gets an equal share of the remaining request deadline, including its
retries. A transient failure or a retry delay longer than that share advances to
the next source. TLS verification failures, permanent HTTP errors and invalid
quotes return UNKNOWN. Each quote response is limited to 64 KiB of decoded data.
When fallbacks are configured, the status identifies the answering source as
`primary`, `fallback1`, and so on, without printing its URL.

### Short-window movement

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Give the monitoring user a private writable state directory on a local Linux or
macOS filesystem. Keep the sibling `.lock` file in place between checks. Use a
separate state file per window. Currencies have independent histories inside it.
The default window is 3600 seconds. Each valid quote needs a vendor timestamp
within the window and the age limit, which is one hour unless `--max-age` sets
another. The plugin compares the current
price with the oldest earlier positive price in that window and reports the
actual elapsed seconds. Repeated timestamps do not create additional samples.
A first sample, expired history, or corrupt JSON starts a new baseline; the
window metric is unknown until there is a comparable sample. Other alerts still
apply. Unwritable state, a symbolic-link state or lock file, or a quote older
than the newest recorded sample returns UNKNOWN. The signed `bitcoin_move_window` metric
uses symmetric warning and critical ranges. Equality at a limit does not alert.

The plugin opens the state directory once per check and works relative to it, so
a path component replaced during the check cannot redirect the lock, the read,
or the write. Symbolic links in the directory part of the path are followed when
the check starts, which keeps platform links such as `/var` on macOS usable. The
state directory and its ancestors must therefore not be writable by other
users. State and lock files are created with mode 0600.

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
| `--currency` | Currency code of 2-16 letters or digits (default: usd) |
| `--timeout` | Total API request/retry budget in seconds, including fractional values (default: 10) |
| `--retries` | Additional transient attempts, 0–5 (default: 1) |
| `--max-age` | Maximum vendor quote age in seconds and require a timestamp; timestamped quotes default to 3600 |
| `--warning-change` | Warning limit for absolute 24-hour percentage movement |
| `--critical-change` | Critical limit for absolute 24-hour percentage movement |
| `--api-url` | Primary API URL |
| `--fallback-url` | Additional compatible endpoint; repeat in preferred order |
| `--state-file` | JSON movement history file |
| `--move-window` | Movement window in seconds (default: 3600) |
| `--warning-move`, `--critical-move` | Absolute window movement thresholds in percent |
| `-v`, `--verbose` | Enable verbose output |
| `-V`, `--version` | Show version |
| `-h`, `--help` | Show help message |

## Nagios Configuration

### Command Definition

Set the Nagios resource macro `$USER1$` to the plugin directory (the native packages use `/usr/lib/nagios/plugins`). Add to your Nagios commands configuration:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
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
numbers, with each low bound no greater than its high bound. The currency must
be 2-16 letters or digits. Invalid configuration is rejected before contacting
the API. Prices must be finite and nonnegative, given as JSON numbers or plain
decimal strings such as `"43521.5"`. A response without the requested currency
names it, for example `Response has no EUR price`. Invalid responses do not emit
performance data. Verbose diagnostics go to stderr
so stdout contains a single monitoring status line.

| Code | Status | Description |
|------|--------|-------------|
| 0 | OK | Price is within acceptable range |
| 1 | WARNING | Price crossed warning threshold |
| 2 | CRITICAL | Price crossed critical threshold |
| 3 | UNKNOWN | Error occurred (API failure, timeout, etc.) |

## Performance Data

The plugin outputs performance data in standard Nagios format:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Price performance data includes the configured warning/critical ranges and a
minimum of zero. Thresholds are printed in full decimal notation, never rounded
or in exponent form, so large values such as `14500000:16250000` stay parseable. Request time includes all attempts and backoff. Quote age is
emitted only when the vendor supplies a valid timestamp; daily change is emitted
when available. Change ranges are symmetric around zero. Invalid or stale data
produces `UNKNOWN` without price performance data. These metrics can be used with
graphing tools like PNP4Nagios, Grafana, or InfluxDB.

## API

This plugin uses the [CoinGecko API](https://www.coingecko.com/en/api) by default, which is free and doesn't require an API key. Rate limits apply.

Custom endpoints must use the same response shape: `bitcoin.<currency>` for
price, `bitcoin.last_updated_at` for UNIX timestamp seconds, and
`bitcoin.<currency>_24h_change` for signed daily percentage movement. Only price
is required when `--max-age` and the change thresholds are absent. A timestamp
that is present is still checked: it must not be in the future or more than one
hour old. The decoded response must fit in 64 KiB.

Supported currencies include: usd, eur, gbp, jpy, aud, cad, chf, cny, and many more.

## Security

The measures below are implemented in the current code. They limit what a misbehaving endpoint or a local user can do to the
monitoring host; they do not make the quote itself trustworthy.

- HTTPS certificates are verified with the `requests` defaults, and no option
  disables verification. A custom `--api-url` that uses plain `http://` has no
  such protection.
- DNS, connection, reads, retries, and backoff share the `--timeout` deadline. A
  peer that sends data slowly cannot extend it.
- Each response is limited to 64 KiB after decompression, and redirect bodies
  are discarded unread.
- Request failures print only an HTTP status or an error class, because a custom
  `--api-url` may contain credentials.
- The command installed by the `.deb` and `.rpm` runs Python in isolated mode.
  It ignores `PYTHONPATH`, the user site directory, and modules in the working
  directory. A `pip` installation uses the standard console script and follows
  the environment it is installed in.
- Movement state is read and written without following a symbolic link at the
  state or lock file name, relative to a directory opened once per check.
- Release assets carry build provenance attestations in addition to
  `SHA256SUMS`; see [From GitHub Releases](#from-github-releases).

## Upgrading from 1.0.0

These changes ship in 2.0.0.

- A quote with a vendor timestamp older than one hour returns `UNKNOWN` unless a
  larger `--max-age` is given. Endpoints that return no timestamp are unaffected.
- `--currency` accepts only 2-16 letters or digits.
- Numeric strings with digit separators or surrounding spaces are rejected.
- A retry wait that does not fit the budget reports the underlying failure
  instead of `API request timed out`.
- The native packages no longer honor `PYTHONPATH`.
- Thresholds of one million or more appear in performance data as plain
  decimals instead of exponent notation.

## Localization

CLI help, validation errors, and plugin status descriptions support 48 locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`) using bundled stdlib-loaded catalogs. Resolution checks `--lang`, then `LC_ALL`, `LC_MESSAGES`, and `LANG`, falling back to `en`. Nagios status prefixes (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) and performance data remain unchanged across all locales.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Development

Install [mise](https://mise.jdx.dev/getting-started.html), then run the development setup above. `mise.toml` pins Python and uv. Development tools are declared in `pyproject.toml` and resolved in the committed `uv.lock`.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Install the commit hooks after setup:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Use `mise exec -- uv add --dev <tool>` or `mise exec -- uv add <dependency>` to update dependencies and commit both `pyproject.toml` and `uv.lock`.

CI checks Python 3.12 and 3.13 on Linux and Python 3.13 on macOS. Every PR also runs package validation, dependency auditing, and CodeQL, and installs the `.deb` on Ubuntu and the `.rpm` on Fedora. Built distributions are available as the `distributions` artifact on CI runs.

The package and CLI version comes from `check_bitcoin_price/__init__.py`. See [the release process](CONTRIBUTING.md#releases) for version bumps and automated publication of GitHub release assets.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow and signed-off commit requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Thomas Vincent

## Acknowledgments

- [CoinGecko](https://www.coingecko.com/) for providing a free cryptocurrency API
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
