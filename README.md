# check_bitcoin_price

A Nagios/Icinga plugin to monitor Bitcoin price with configurable warning and critical thresholds.

[![Python Version](https://img.shields.io/pypi/pyversions/check-bitcoin-price.svg)](https://pypi.org/project/check-bitcoin-price/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- Monitor Bitcoin price in multiple currencies (USD, EUR, GBP, etc.)
- Configurable warning and critical thresholds (high and low)
- Standard Nagios plugin output with performance data
- Uses CoinGecko API (free, no API key required)
- Support for custom API endpoints
- Configurable timeout

## Installation

### From PyPI

```bash
pip install check-bitcoin-price
```

### From Source

```bash
git clone https://github.com/thomasvincent/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### For Development

```bash
git clone https://github.com/thomasvincent/check_bitcoin_price.git
cd check_bitcoin_price
pip install -e ".[dev]"
```

## Usage

### Basic Usage

```bash
# Check Bitcoin price (no thresholds - always returns OK)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00
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
# Set timeout to 30 seconds
check_bitcoin_price --timeout 30
```

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
| `--timeout` | API request timeout in seconds (default: 10) |
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

| Code | Status | Description |
|------|--------|-------------|
| 0 | OK | Price is within acceptable range |
| 1 | WARNING | Price crossed warning threshold |
| 2 | CRITICAL | Price crossed critical threshold |
| 3 | UNKNOWN | Error occurred (API failure, timeout, etc.) |

## Performance Data

The plugin outputs performance data in standard Nagios format:

```
bitcoin_price=43521.00
```

This can be used with graphing tools like PNP4Nagios, Grafana, or InfluxDB.

## API

This plugin uses the [CoinGecko API](https://www.coingecko.com/en/api) by default, which is free and doesn't require an API key. Rate limits apply.

Supported currencies include: usd, eur, gbp, jpy, aud, cad, chf, cny, and many more.

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
ruff format check_bitcoin_price tests
```

### Linting

```bash
ruff check check_bitcoin_price tests
```

### Type Checking

```bash
mypy check_bitcoin_price
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Thomas Vincent

## Acknowledgments

- [CoinGecko](https://www.coingecko.com/) for providing a free cryptocurrency API
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
