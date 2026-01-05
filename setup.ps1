# PowerShell script for Windows users
param()

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

Write-Host "Setup complete. Activate with: .\.venv\Scripts\Activate.ps1"