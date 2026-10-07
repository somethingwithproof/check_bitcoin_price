<!--
SPDX-FileCopyrightText: 2024 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# check_bitcoin_price coding guide

Read [AGENTS.md](AGENTS.md) before making changes. It contains the repository's
architecture, canonical commands, supported boundaries and operating rules.
Follow any applicable nested instructions and the checked-out CI configuration.

## Project priorities

Review quote freshness, currency consistency, signed movement, highest severity and total request deadlines.

## Verification

`mise run check`, `mise run test`, `mise run audit` and `mise run build`, invoked as separate tasks.

Separate offline checks from operations that change hosts, databases, firewalls
or published artifacts. State verification limits and preserve existing controls.
Select language runtimes through `mise`; never commit local session state or secrets.
