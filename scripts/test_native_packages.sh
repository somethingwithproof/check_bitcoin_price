#!/usr/bin/env bash
set -euo pipefail

# Ubuntu 24.04 supplies Python 3.12; apt resolves the declared dependencies.
sudo apt-get update -qq
sudo apt-get install --yes ./dist/*.deb
check_bitcoin_price --version
/usr/lib/nagios/plugins/check_bitcoin_price --help

# Test RPM installation and dependency resolution on a native Fedora system.
docker run --rm --volume "$PWD/dist:/packages:ro" fedora:43 \
  bash -euo pipefail -c '
    dnf install --assumeyes /packages/*.rpm
    check_bitcoin_price --version
    /usr/lib/nagios/plugins/check_bitcoin_price --help
  '
