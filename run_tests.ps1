Param()
Set-StrictMode -Version Latest
$Venv = ".venv"
if (Test-Path $Venv) {
    # activate
    . "${Venv}\Scripts\Activate.ps1"
}

pytest -q
