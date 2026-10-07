<!--
SPDX-FileCopyrightText: 2024 Thomas Vincent
SPDX-License-Identifier: MIT
-->

# check_bitcoin_price implementation and review instructions

Read [AGENTS.md](../AGENTS.md) for the complete repository-specific guidance.

## Review priorities

Review quote freshness, currency consistency, signed movement, highest severity and total request deadlines.

Require focused regression evidence for changed behavior and preserve existing
correctness/security checks. `mise run check`, `mise run test`, `mise run audit` and `mise run build`, invoked as separate tasks.

Flag unsupported maturity claims, hidden failures, credentials in code/logs, and
generated output presented as first-party implementation. Review permissions,
immutable Action pins and fork-secret isolation when workflows change. A skipped
check or absent check result is not proof that validation ran.

Keep changes within the requested scope and use `mise` for language runtimes.
