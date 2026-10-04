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

## Releases

Stable releases use SemVer `MAJOR.MINOR.PATCH`: increment MAJOR for incompatible CLI/output behavior, MINOR for compatible new features, and PATCH for compatible fixes. Prerelease and build-metadata tags are not published by this workflow.

1. Update `__version__` in `check_bitcoin_price/__init__.py` in a PR. This is the sole version source for the CLI, Python distributions, and native packages.
2. Run `mise run package` locally; CI also installs the Debian package on Ubuntu and the RPM package on Fedora. Merge the version PR after checks pass.
3. From the merged commit on `main`, create and push the matching annotated tag:

   ```bash
   git tag -a v1.0.0 -m 'Release v1.0.0'
   git push origin v1.0.0
   ```

The Release workflow rejects invalid tags, package/tag version mismatches, and commits outside `main`. It reruns lint, types, tests, coverage, and security audits; builds the wheel, source `.tar.gz`, architecture-independent `.deb` and `.rpm`; and tests native installation before publishing. GitHub generates release notes from merged PRs. `SHA256SUMS` covers all four assets.

Publication creates a draft with assets first, then publishes the completed release. Retry a failed run in Actions, or run the Release workflow manually with the existing tag. An unfinished draft can resume; published releases and their assets are not overwritten. Fix a published defect in a new PATCH release. The workflow requires only the repository's built-in GitHub token and does not upload packages to PyPI.
