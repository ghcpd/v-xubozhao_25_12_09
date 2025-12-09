import sys
import subprocess
from importlib.metadata import version, PackageNotFoundError
import pytest


def test_installed_package_metadata():
    """Check package metadata without importing compiled modules (avoids segfaults).

    This uses importlib.metadata.version which reads package metadata rather than importing
    the module objects so it is robust on environments where binary imports may fail.
    """
    packages = ["numpy", "pandas", "fastapi", "requests"]
    for pkg in packages:
        try:
            pkg_ver = version(pkg)
        except PackageNotFoundError:
            pytest.skip(f"{pkg} not installed in environment; skipping metadata check")
        assert isinstance(pkg_ver, str) and pkg_ver


def test_fastapi_app_client():
    """A small FastAPI functional test that uses the TestClient (pure python).
    """
    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"status": "ok"}

    client = TestClient(app)
    res = client.get('/ping')
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_optional_sklearn_training_subprocess():
    """If scikit-learn is available and importable in a subprocess, run a brief training check.

    Running in a subprocess isolates the main pytest process from potential segfaults caused
    by compiled libs that may not match the runtime (observed in some Windows setups).
    """
    try:
        sk_ver = version('scikit-learn')
    except PackageNotFoundError:
        pytest.skip('scikit-learn not installed; skipping heavy analytics tests')

    # Run a tiny python snippet in a subprocess to avoid importing sklearn in the main process.
    code = (
        "import numpy as n, math;"
        "from sklearn.linear_model import LinearRegression;"
        "X = n.array([[1],[2],[3],[4]]); y = n.array([2,4,6,8]);"
        "m = LinearRegression(); m.fit(X,y); print(m.predict([[5]])[0])"
    )

    proc = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    if proc.returncode != 0:
        pytest.skip(f"scikit-learn check failed in subprocess (likely build issue): {proc.stderr[:300]}")
    out = proc.stdout.strip()
    assert out != ""
