# CLAUDE.md

Nagios/Icinga monitoring plugin for Bitcoin price alerts.

## Stack
- Python 3.8+

## Lint & Test
```bash
pytest
black check_bitcoin_price tests
isort check_bitcoin_price tests
mypy check_bitcoin_price
flake8 check_bitcoin_price tests
```

## Local Test
```bash
# Simulate monitoring check
check_bitcoin_price -w 30000:50000 -c 25000:60000
```
