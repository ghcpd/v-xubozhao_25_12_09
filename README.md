# oswe-mini-secondary - dependency upgrade + pytest harness

This workspace is a small maintenance project to update an old project's Python dependencies and provide a reproducible pytest-based validation harness.

Quick steps (POSIX/macOS/Linux):

1. Create a venv & install pinned dependencies

```bash
./setup.sh
```

2. Run the test suite

```bash
./run_tests.sh
```

3. Run the demo script (inside activated venv)

```bash
source .venv/bin/activate
python demos/demo_basic_usage.py
```

Notes:
- Provided `requirements.txt` contains modern, pinned versions that are Python 3.10+ compatible.
- Tests are written with pytest in `tests/test_runtime.py`.
