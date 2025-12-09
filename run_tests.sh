#!/usr/bin/env bash
set -euo pipefail

VENV_DIR=.venv
if [ ! -d "${VENV_DIR}" ]; then
  echo "Virtual env not found. Run ./setup.sh first to create ${VENV_DIR}."
  exit 2
fi

source "${VENV_DIR}/bin/activate"
echo "Running pytest..."
pytest -q -ra
#!/usr/bin/env bash
set -euo pipefail

VENV_DIR=".venv"
if [ -d "$VENV_DIR" ]; then
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
fi

pytest -q
