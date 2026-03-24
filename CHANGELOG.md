# Changelog

All notable changes to this project will be documented in this file.

## [0.5.0] - 2026-03-24

### Added
- Public API exports in `spadesdk/__init__.py` — all core classes now importable from the top-level package (`Executor`, `Process`, `RunResult`, `File`, `FileProcessor`, `FileUpload`, `HistoryProvider`, `User`)
- Test suite with 27 tests covering `Executor`, `FileProcessor`, `HistoryProvider`, `User`, and public API surface
- `pytest>=8.0` dev dependency in `pyproject.toml`
- GitHub Actions release workflow — publishes to PyPI on version tag push using OIDC trusted publishing

### Changed
- `RunResult.user_id: int | None` renamed to `RunResult.user: User | None` — passes the full `User` object instead of just the ID
- `Executor.run()` signature updated: `user_id: int` parameter replaced with `user: User`
- Pre-commit hooks updated: `pre-commit-hooks` v5.0.0 → v6.0.0, `ruff-pre-commit` v0.11.13 → v0.15.7

### Fixed
- `FileProcessor.validate()` now raises `ValueError` when `file.schema is None` instead of passing `None` to `from_frictionless_schema`
- Fixed typo in README.md: `https:://getspade.io` → `https://getspade.io`

## [0.4.0] - 2024-XX-XX

- See git history for previous changes.
