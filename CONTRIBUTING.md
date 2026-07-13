# Contributing to xyzgeom

Thanks for considering a contribution. This project is intentionally small — please keep changes focused and in scope (basic .xyz geometry calculations), rather than adding new features like trajectory support or plotting.

## Setup

```bash
git clone https://github.com/sidd265/xyzgeom.git
cd xyzgeom
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e ".[dev]"
pre-commit install
```

`pre-commit install` sets up git hooks so ruff and mypy run automatically before each commit, catching issues before they reach CI.

## Making a change

1. Create a branch off `main` named `<type>/<short-description>`, e.g. `fix/angle-rounding`.
2. Make your change, adding or updating tests as needed. Every bug fix or feature should have a test that would fail without it.
3. Run the full check suite locally:
   ```bash
   ruff check .
   ruff format --check .
   mypy
   pytest
   ```
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/) style: `feat: ...`, `fix: ...`, `test: ...`, `docs: ...`, `chore: ...`, `ci: ...`.
5. Push your branch and open a pull request against `main`. CI must pass before merge.

## Code style

- Type hints are required on all public functions; `mypy --strict` must pass.
- Formatting and linting are enforced by `ruff` (see `pyproject.toml` for config) — run `ruff format .` to auto-fix formatting.

## Reporting bugs

Please open an issue using the bug report template and include a minimal `.xyz` snippet that reproduces the problem where possible.
