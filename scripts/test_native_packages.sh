#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

set -euo pipefail

# Resolve the command exactly as documented for a packaged Nagios installation.
documented=$(awk '/command_line .*check_bitcoin_price/{print $2; exit}' README.md)
test "$documented" = '$USER1$/check_bitcoin_price'
plugin="/usr/lib/nagios/plugins/${documented#*/}"

# Ubuntu 24.04 supplies Python 3.12; apt resolves the declared dependencies.
sudo apt-get update -qq
sudo apt-get install --yes ./dist/*.deb
check_bitcoin_price --version
"$plugin" --help

# Test RPM installation and dependency resolution on a native Fedora system.
docker run --rm --env "plugin=$plugin" --volume "$PWD/dist:/packages:ro" fedora:43 \
  bash -euo pipefail -c '
    dnf install --assumeyes /packages/*.rpm
    check_bitcoin_price --version
    "$plugin" --help
  '
