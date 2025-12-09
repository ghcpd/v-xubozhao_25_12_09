#!/bin/bash
# Test runner script: Execute pytest with detailed output
# Usage: bash run_tests.sh

set -e  # Exit on error

# Activate venv
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo "🧪 Running pytest test suite..."
echo "================================================"

# Run pytest with verbose output, coverage, and detailed reports
pytest tests/ \
    -v \
    --tb=short \
    --color=yes \
    --junit-xml=test-results.xml \
    --html=test-results.html \
    --self-contained-html \
    2>&1 | tee test_run.log

TEST_RESULT=$?

echo ""
echo "================================================"
if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "❌ Tests failed! Check test_run.log for details."
fi
echo "================================================"
echo ""
echo "📊 Test Reports:"
echo "  - Console output: test_run.log"
echo "  - JUnit XML: test-results.xml"
echo "  - HTML Report: test-results.html"

exit $TEST_RESULT
