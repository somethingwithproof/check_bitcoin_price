# Contributing

Create a branch from `main` and keep each pull request focused on one change.

## Setup and verification

Install mise, then run:

```bash
mise trust
mise install
mise run setup
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise run check
mise run test
mise run audit
mise run build
```

Run `mise run format` to format Python code. Tests use mocked responses or a local HTTP server; they must not depend on live market prices or vendor availability.

Declare runtime dependencies in `project.dependencies` and development tools in `dependency-groups.dev` in `pyproject.toml`. Regenerate `uv.lock` with `mise exec -- uv lock` and include it with dependency changes. Local hooks use the same locked Python tools as CI.

## Pull requests

Describe the behavior that changed and the checks you ran. Add regression coverage for behavior changes, preserve Nagios exit codes and performance-data conventions, and document new CLI options.

Sign off each commit for the Developer Certificate of Origin using `git commit -s`. Open the PR against `main` and wait for CI and security checks before merging.

Dependabot updates run weekly. The scheduled merge workflow accepts only non-draft Dependabot PRs with passing or skipped checks and verifies the commit SHA at merge time. Failed, pending, missing, or unrecognized check results prevent automatic merging.
