#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

set -euo pipefail

# The packaged command must not import modules from the directory it runs in.
planted=$(mktemp -d)
chmod 755 "$planted"
echo 'raise SystemExit("imported requests from the working directory")' > "$planted/requests.py"

# Ubuntu 24.04 supplies Python 3.12; apt resolves the declared dependencies.
sudo apt-get update -qq
sudo apt-get install --yes ./dist/*.deb
check_bitcoin_price --version
/usr/lib/nagios/plugins/check_bitcoin_price --help
(cd "$planted" && PYTHONPATH="$planted" check_bitcoin_price --version)

# Test RPM installation and dependency resolution on a native Fedora system.
docker run --rm --volume "$PWD/dist:/packages:ro" \
  --volume "$planted:/planted:ro" fedora:43 \
  bash -euo pipefail -c '
    dnf install --assumeyes /packages/*.rpm
    check_bitcoin_price --version
    /usr/lib/nagios/plugins/check_bitcoin_price --help
    /usr/lib64/nagios/plugins/check_bitcoin_price --help
    cd /planted && PYTHONPATH=/planted check_bitcoin_price --version
  '
