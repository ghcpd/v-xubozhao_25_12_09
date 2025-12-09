#!/usr/bin/env bash
# Create a reproducible venv and install pinned dependencies
set -euo pipefail

PYTHON=${PYTHON:-python}
VENV_DIR=.venv

echo "Creating virtual environment in ${VENV_DIR} using ${PYTHON}..."
${PYTHON} -m venv "${VENV_DIR}"
echo "Activating virtual environment and upgrading pip..."
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"
python -m pip install --upgrade pip setuptools wheel
echo "Installing pinned project requirements from requirements.txt"
pip install -r requirements.txt
echo "Setup complete. Activate with: source ${VENV_DIR}/bin/activate"
#!/usr/bin/env bash
set -euo pipefail

VENV_DIR=".venv"

python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip
pip install -r requirements.txt
echo "Environment created in $VENV_DIR and packages installed via requirements.txt"
