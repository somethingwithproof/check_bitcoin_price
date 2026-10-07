<!--
SPDX-FileCopyrightText: 2024 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# Bitcoin price checker agent instructions

## Purpose and layout

This Python Nagios/Icinga plugin checks Bitcoin quotes, freshness and configured
price/movement thresholds. `check_bitcoin_price/plugin.py` owns CLI/status
handling; `quotes.py` validates quote semantics; `transport.py` bounds HTTP
requests and retries. `pyproject.toml` declares the installed CLI and tooling;
`tests/` covers plugin contracts, transport boundaries, CLI and release validation.

## Canonical commands

Read `CONTRIBUTING.md` and use versions from `mise.toml`. `uv.lock` is the
reproducible dependency authority; do not restore removed requirements files or
install unbounded tools to work around the lock.

```sh
mise install
mise run check
mise run test
mise run audit
mise run build
```

Run tasks separately, or use mise's task separator; extra words after one task
name are arguments to that task. The setup dependency installs frozen tools.
`mise run format` applies formatting; `mise run package` also builds native
packages. Those commands do not authorize release publication.

## Monitoring and transport contracts

Preserve Nagios exit codes, single status-line output, performance data and
existing CLI aliases. Stale/future/malformed/missing prices or timestamps must
not imply OK. Match movement data to the selected currency; retain signed
movement and highest-severity behavior. Bound the total retry deadline and
response size; preserve TLS verification and safe error messages.

Tests must use mocked responses or a local HTTP server, never live market data
or stored vendor credentials. Keep meaningful coverage/failure-path tests; do
not weaken the configured threshold to accommodate new code.

## Packaging and release

The version in `check_bitcoin_price/__init__.py` is the sole version source.
`packaging/nfpm.yaml` and `scripts/build_native_packages.py` create native
packages; `scripts/validate_release.py` checks stable SemVer tags. Preserve
wheel/source/deb/rpm verification, `SHA256SUMS` and exact-main-tag publication.
Follow `CONTRIBUTING.md` for authorized releases; never overwrite published assets.

## Working rules

Select required language runtimes through `mise`. Read the checked-out manifests,
lockfiles and GitHub Actions before choosing versions or commands; do not infer
support from an old README example. Keep changes focused and preserve public
interfaces, licenses and existing correctness/security checks.

Keep credentials, customer data, `.omc/`, `.worktrees/` and generated output out
of commits. Never disable checks or suppress findings just to obtain a passing
result. Report the commands run, results and untested environments. Publishing,
deploying, modifying live systems and merging require task authorization.
