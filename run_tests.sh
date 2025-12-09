#!/usr/bin/env bash
set -euo pipefail

# Activate venv then run pytest
if [ -f .venv/bin/activate ]; then
  . .venv/bin/activate
fi

pytest -q --maxfail=1
