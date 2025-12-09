"""
conftest.py - Pytest configuration and shared fixtures
"""

import pytest


@pytest.fixture(scope="session")
def suppress_warnings():
    """Suppress non-critical deprecation warnings during testing"""
    import warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)
