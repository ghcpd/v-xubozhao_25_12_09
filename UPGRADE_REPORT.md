# Dependency Upgrade Report

## Overview
Upgraded project dependencies to be Python 3.10+ compatible and remove known insecure/outdated versions. Added reproducible pinned requirements and CI-friendly test scripts using pytest.

## Before → After

- scikit-learn: 0.24.1 -> 1.2.2
  - Justification: Many performance and bug fixes; support for current numpy/scipy; minor API changes (e.g., default `n_jobs` behavior, some deprecations) — verified tests and demo.

- numpy: 1.18.0 -> 1.24.3
  - Justification: Security and performance updates; modern CPUs better optimized; Python 3.10+ compatibility.

- pandas: 1.1.5 -> 1.5.3
  - Justification: Bug fixes, new features, maintained on Python 3.10; many deprecations removed — none affect our minimal usage.

- matplotlib: 3.3.2 -> 3.5.3
  - Justification: Compatibility with newer pandas/numpy and bug fixes.

- scipy: 1.5.2 -> 1.9.3
  - Justification: Performance and stability improvements; Python 3.10 support.

- pytest: 5.4.3 -> 7.4.0
  - Justification: Newer pytest adds improved fixtures and security fixes; migration notes considered (minor plugins may need updates).

- fastapi: 0.63.0 -> 0.95.1
  - Justification: Many bug fixes and features; ensures support for modern ASGI servers and Pydantic 1.10.x.

- uvicorn: 0.13.3 -> 0.20.0
  - Justification: Performance and security improvements for ASGI server.

## Breaking/Compatibility Notes
- scikit-learn: 1.x introduces some changed defaults and deprecation cycles; our codebase uses common APIs (fit/predict) which are stable. If advanced models or deprecated functions are used elsewhere, test coverage should be extended.
- pandas: Several API deprecations between 1.1 and 1.5 (e.g., `.astype` warnings, index behaviors); add tests for code paths manipulating datetime and indices.
- fastapi/pydantic: We pinned FastAPI to a version using pydantic<2 to avoid migrating to Pydantic v2 (major rewrite). When upgrading to FastAPI versions that require Pydantic v2, plan an application audit.

## Reproducibility
- requirements.txt pins exact versions.
- setup.sh installs into a local virtual environment `.venv`.

## Automated Tests and Scripts
- setup.sh  — create venv, install deps
- run_tests.sh — run pytest
- demo.py — small scikit-learn demo to sanity-check key libs
- tests/test_runtime.py — pytest tests covering basic imports and small ML pipeline

## Results
All tests executed in a fresh `.venv` and passed:

5 passed in 21.25s

## Recommendations
- Add continuous integration (GitHub Actions) that runs setup.sh and run_tests.sh on every PR.
- Consider adding pinned hash-file (pip hash or pip-compile output) if stricter reproducibility is needed.
- Extend test coverage to cover library-specific features used by the app.

