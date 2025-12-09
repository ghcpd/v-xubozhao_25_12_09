#!/bin/bash
# Setup script: Create venv and install dependencies
# Usage: bash setup.sh

set -e  # Exit on error

echo "🔧 Setting up Python analytics environment..."
echo "================================================"

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv venv

# Activate venv
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    echo "🪟 Detected Windows environment"
    source venv/Scripts/activate
else
    echo "🐧 Detected Unix environment"
    source venv/bin/activate
fi

# Upgrade pip
echo "🆙 Upgrading pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel

# Install dependencies
echo "📥 Installing requirements..."
pip install -r requirements.txt

# Verify installation
echo "✅ Verifying installed packages..."
pip list

echo ""
echo "✨ Setup complete!"
echo "================================================"
echo "To activate the environment, run:"
echo "  source venv/bin/activate  (Linux/macOS)"
echo "  .\\venv\\Scripts\\activate  (Windows)"
echo ""
echo "To run tests, execute:"
echo "  bash run_tests.sh"
