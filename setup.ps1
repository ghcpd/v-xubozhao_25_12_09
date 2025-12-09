Param()
Set-StrictMode -Version Latest
$Venv = ".venv"

python -m venv $Venv
Push-Location $Venv
if (Test-Path -Path "Scripts/Activate.ps1") {
    # Activate in current session for the remainder of the script
    . "Scripts/Activate.ps1"
}
python -m pip install --upgrade pip
python -m pip install -r "..\requirements.txt"
Pop-Location
Write-Host "Environment created in $Venv and packages installed via requirements.txt"
