# Dependency audit — Before → After

Below is a concise audit of the old dependencies (from `requirements_old.txt`) and the proposed upgrades in `requirements.txt`.

## Before (requirements_old.txt)
```
scikit-learn==0.24.1
numpy==1.18.0
pandas==1.1.5
matplotlib==3.3.2
scipy==1.5.2
pytest==5.4.3
fastapi==0.63.0
uvicorn==0.13.3
```

## After (requirements.txt)
```
scikit-learn==1.3.2
numpy==1.25.3
pandas==2.2.3
matplotlib==3.7.2
scipy==1.11.3
pytest==8.4.3
fastapi==0.95.2
uvicorn==0.22.0
```

## Rationales and notes

- numpy 1.18.0 → 1.25.3
  - 1.18 is >5 years old and lacks many performance and ABI improvements that modern SciPy and scikit-learn expect.
  - Newer numpy releases are compiled against modern C runtimes and provide better performance and compatibility with Python 3.10+.

- scikit-learn 0.24.1 → 1.3.2
  - 0.24 series predates the 1.0 breaking-release. Upgrading to 1.3.x brings performance improvements, fixes, and Python 3.10+ compatibility.
  - Some APIs changed across 1.x merges (notably deprecations removed in 1.2+); tests should check the code paths used.

- pandas 1.1.5 → 2.2.3
  - 1.1.x doesn't support newer typing and performance improvements; pandas 2.x changed some internals and improved type handling.

- scipy 1.5.2 → 1.11.3
  - SciPy 1.5.x is old; newer SciPy versions include performance and compatibility fixes used by modern scikit-learn.

- matplotlib 3.3.2 → 3.7.2
  - Keeps plotting compatibility but picks up important bugfixes.

- pytest 5.4.3 → 8.4.3
  - Up-to-date pytest provides better fixtures, faster runs and official Python 3.10+ compatibility.

- fastapi 0.63.0 → 0.95.2 and uvicorn 0.13.3 → 0.22.0
  - Many internal improvements and dependency updates. Newer FastAPI relies on Starlette versions and uvicorn updates that are more secure.

## Upgrade risk summary

- Major changes: scikit-learn (0.24 -> 1.3) and pandas (1.1 -> 2.2) are the highest risk for breaking changes — please run code-level tests against workflows (ML training, model persistence, data parsing).
- Runtime environment: target is Python 3.10+ and Linux/macOS/Windows with proper C-compiled wheel availability. These pinned versions work well with Python 3.10.

## Next steps

- Add reproducible installation and automated tests (setup scripts and pytest tests) to confirm the updated environment works for the most common runtime patterns.
