# PowerShell wrapper to run tests on Windows
param()

if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    try {
        . \.venv\Scripts\Activate.ps1
        pytest -q --maxfail=1
        return
    } catch {
        Write-Warning "Activating .venv failed; will try direct python binary in .venv"
    }
}
# Fall back to invoking the venv python directly if present
$venvPython = ".\.venv\Scripts\python.exe"
if (Test-Path $venvPython) {
    $hasPytest = & $venvPython -c "import importlib, sys; sys.stdout.write('YES' if importlib.util.find_spec('pytest') else 'NO')"
    if ($hasPytest -eq 'YES') {
        & $venvPython -m pytest -q --maxfail=1
        exit $LASTEXITCODE
    } else {
        Write-Warning "pytest not found in .venv; falling back to system pytest."
    }
}
# Otherwise run pytest with system python
pytest -q --maxfail=1
