#!/usr/bin/env bash
set -euo pipefail

# Create virtual environment and install pinned dependencies
PY=python3
if command -v python3 &>/dev/null; then
  PY=python3
elif command -v python &>/dev/null; then
  PY=python
fi

$PY -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Verify installations
pip check || true

echo "Setup complete. Activate with: source .venv/bin/activate"