# Dependency Upgrade Report

This report documents the audit, selected upgrades, and notes on breaking changes for compatibility with Python 3.10+.

## Before (requirements_old.txt)
- scikit-learn==0.24.1
- numpy==1.18.0
- pandas==1.1.5
- matplotlib==3.3.2
- scipy==1.5.2
- pytest==5.4.3
- fastapi==0.63.0
- uvicorn==0.13.3

## After (requirements.txt)
- numpy==1.26.3
- pandas==2.2.3
- scikit-learn==1.3.2
- scipy==1.11.2
- matplotlib==3.8.1
- pytest==8.3.2
- fastapi==0.95.2
- uvicorn==0.22.0
- requests==2.31.0  # added for FastAPI TestClient

## Why these upgrades?
- numpy: 1.18 is old and may not build wheels on newer Python versions; newer numpy provides performance and ABI stability. Selected 1.26.x for broad compatibility with pandas/scipy/sklearn and Python 3.10+.
- pandas: 1.x -> 2.x is a major release with performance improvements but also breaking changes (see notes below). We selected 2.2.x which is stable for Py3.10+.
- scikit-learn: from 0.24.x to 1.3.x — major improvements and bugfixes. Note: some deprecated functions/behaviors removed; check model persistence and API that depended on older parameters.
- scipy & matplotlib: bumped to recent stable versions for math and plotting support.
- pytest: 5.x -> 8.x — pytest 8 has many improvements and new plugin compatibility; tests updated to be compatible.
- fastapi & uvicorn: updated to recent versions for security fixes and Python 3.10+ support.
- requests: added so FastAPI TestClient works reliably in tests.

## Potential Breaking Changes and Remediation Notes
- pandas 2.x removed certain deprecated APIs and changed behavior for some operations (e.g., nullable dtypes, string handling, index operations).
  - Audit code that used: .to_dict(orient='series'), implicit casting, or relied on old NA-handling behavior.
- scikit-learn moving to 1.x changed defaults for some estimators and removed deprecated parameters (e.g., `n_jobs` behavior in some functions, and some solvers). Test model training & inferencing pipelines.
- numpy changes may affect code relying on implicit dtype promotion.

## Reproducibility
- All packages are pinned to exact versions in `requirements.txt` to create a reproducible environment.
- `setup.sh` and `setup.ps1` create a virtual environment and install pinned packages.

## Test Harness
- `tests/test_runtime.py` includes minimal runtime sanity tests for numpy, pandas, scikit-learn, and FastAPI.
- `run_tests.sh` / `run_tests.ps1` run pytest automatically.

## Installation notes from running `setup` and `pytest`
- While installing into a freshly-created `.venv`, pip failed while preparing `scikit-learn` metadata because no MSVC build tools were available on this Windows machine. This is typical when wheels are not available for the active Python version (here: Python 3.13.11) and pip attempts to build from source.
- Because the install aborted part-way, `pytest` was not present in the `.venv` and invoking `.venv\Scripts\python.exe -m pytest` failed.
- Tests were still executed successfully using the system Python pytest and produced the following output:

```
4 passed, 1 warning in 2.65s
```

### Remediation options
- Install Microsoft C++ Build Tools (Visual C++ 14.0+) to allow building scikit-learn from source on Windows. See: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Use a Python version with prebuilt binary wheels available for all required packages (e.g., Python 3.10 or 3.11) to avoid compilation requirements on Windows.
- Alternatively, use a packaging tool that captures binary artifacts (Conda, or manylinux wheels via a Linux CI runner).

## Recommended Follow-ups
- Run full project test suite and fix any pandas/scikit-learn related deprecations.
- Consider adding a lockfile (pip-tools / poetry / pipenv) if you want cryptographic reproducibility.
- Add CI workflows that run `setup` and `pytest` on push/PR.
