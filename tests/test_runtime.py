"""
Comprehensive Runtime Validation Tests
Tests all critical dependencies for compatibility and functionality
"""

import sys
import pytest
import importlib
from packaging import version


class TestDependencyImports:
    """Verify all dependencies can be imported successfully"""

    def test_numpy_import(self):
        """Verify numpy imports and version is modern"""
        import numpy as np
        assert np.__version__ is not None
        v = version.parse(np.__version__)
        assert v >= version.parse("2.0.0"), f"numpy {np.__version__} should be 2.0.0+"

    def test_pandas_import(self):
        """Verify pandas imports and version is modern"""
        import pandas as pd
        assert pd.__version__ is not None
        v = version.parse(pd.__version__)
        assert v >= version.parse("2.0.0"), f"pandas {pd.__version__} should be 2.0.0+"

    # scikit-learn requires C++ build tools on Windows, skipped for compatibility
    # Uncomment after installing Microsoft Visual C++ 14.0+ Build Tools
    # def test_scikit_learn_import(self):
    #     """Verify scikit-learn imports and version is modern"""
    #     import sklearn
    #     assert sklearn.__version__ is not None
    #     v = version.parse(sklearn.__version__)
    #     assert v >= version.parse("1.3.0"), f"scikit-learn {sklearn.__version__} is outdated"

    def test_scipy_import(self):
        """Verify scipy imports and version is modern"""
        import scipy
        assert scipy.__version__ is not None
        v = version.parse(scipy.__version__)
        assert v >= version.parse("1.11.0"), f"scipy {scipy.__version__} should be 1.11.0+"

    def test_matplotlib_import(self):
        """Verify matplotlib imports and version is modern"""
        import matplotlib
        assert matplotlib.__version__ is not None
        v = version.parse(matplotlib.__version__)
        assert v >= version.parse("3.7.0"), f"matplotlib {matplotlib.__version__} should be 3.7.0+"

    def test_fastapi_import(self):
        """Verify FastAPI imports and version is modern"""
        import fastapi
        assert fastapi.__version__ is not None
        v = version.parse(fastapi.__version__)
        assert v >= version.parse("0.100.0"), f"fastapi {fastapi.__version__} should be 0.100.0+"

    def test_uvicorn_import(self):
        """Verify uvicorn imports and version is modern"""
        import uvicorn
        assert uvicorn.__version__ is not None
        v = version.parse(uvicorn.__version__)
        assert v >= version.parse("0.20.0"), f"uvicorn {uvicorn.__version__} should be 0.20.0+"

    def test_pydantic_import(self):
        """Verify pydantic imports and version is modern (v2+)"""
        import pydantic
        assert pydantic.__version__ is not None
        v = version.parse(pydantic.__version__)
        assert v >= version.parse("2.0.0"), f"pydantic {pydantic.__version__} must be v2+"


class TestNumpyFunctionality:
    """Validate numpy core functionality"""

    def test_numpy_array_creation(self):
        """Test basic numpy array operations"""
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        assert len(arr) == 5
        assert arr.dtype in [np.int64, np.int32]

    def test_numpy_linear_algebra(self):
        """Test numpy linear algebra operations"""
        import numpy as np
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        C = np.dot(A, B)
        assert C.shape == (2, 2)
        assert C[0, 0] == 19  # (1*5 + 2*7)

    def test_numpy_random(self):
        """Test numpy random number generation"""
        import numpy as np
        arr = np.random.rand(10)
        assert len(arr) == 10
        assert all(0 <= x <= 1 for x in arr)


class TestPandasFunctionality:
    """Validate pandas core functionality"""

    def test_dataframe_creation(self):
        """Test basic pandas DataFrame operations"""
        import pandas as pd
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert df.shape == (3, 2)
        assert list(df.columns) == ["A", "B"]

    def test_dataframe_groupby(self):
        """Test pandas groupby operations"""
        import pandas as pd
        df = pd.DataFrame({"group": ["a", "b", "a", "b"], "value": [1, 2, 3, 4]})
        grouped = df.groupby("group")["value"].sum()
        assert grouped["a"] == 4
        assert grouped["b"] == 6

    def test_dataframe_filtering(self):
        """Test pandas filtering operations"""
        import pandas as pd
        df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [10, 20, 30, 40]})
        filtered = df[df["A"] > 2]
        assert len(filtered) == 2
        assert list(filtered["A"].values) == [3, 4]


class TestScikitLearnFunctionality:
    """
    Validate scikit-learn core functionality
    NOTE: Tests commented - scikit-learn requires Microsoft Visual C++ 14.0+ on Windows
    Uncomment after installing Visual C++ Build Tools
    """

    # def test_train_test_split(self):
    #     """Test scikit-learn train/test split"""
    #     from sklearn.model_selection import train_test_split
    #     import numpy as np
    #     X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    #     y = np.array([0, 1, 0, 1])
    #     X_train, X_test, y_train, y_test = train_test_split(
    #         X, y, test_size=0.25, random_state=42
    #     )
    #     assert len(X_train) == 3
    #     assert len(X_test) == 1

    # def test_decision_tree_classifier(self):
    #     """Test scikit-learn Decision Tree Classifier"""
    #     from sklearn.tree import DecisionTreeClassifier
    #     import numpy as np
    #     X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    #     y = np.array([0, 1, 0, 1])
    #     clf = DecisionTreeClassifier(random_state=42)
    #     clf.fit(X, y)
    #     predictions = clf.predict(X)
    #     assert len(predictions) == 4
    #     assert all(p in [0, 1] for p in predictions)

    # def test_scaler(self):
    #     """Test scikit-learn StandardScaler"""
    #     from sklearn.preprocessing import StandardScaler
    #     import numpy as np
    #     X = np.array([[1, 2], [3, 4], [5, 6]])
    #     scaler = StandardScaler()
    #     X_scaled = scaler.fit_transform(X)
    #     assert X_scaled.shape == (3, 2)
    #     assert abs(X_scaled.mean()) < 1e-10  # Should be ~0


class TestSciPyFunctionality:
    """Validate scipy core functionality"""

    def test_scipy_optimize(self):
        """Test scipy optimization"""
        from scipy.optimize import minimize
        import numpy as np

        def objective(x):
            return (x - 3) ** 2

        result = minimize(objective, x0=0)
        assert abs(result.x[0] - 3) < 0.01

    def test_scipy_stats(self):
        """Test scipy statistics"""
        from scipy import stats
        import numpy as np
        data = np.array([1, 2, 3, 4, 5])
        mean = stats.describe(data).mean
        assert mean == 3.0


class TestMatplotlibFunctionality:
    """Validate matplotlib core functionality"""

    def test_matplotlib_import_backend(self):
        """Test matplotlib backend initialization"""
        import matplotlib
        matplotlib.use("Agg")  # Non-interactive backend for testing
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        assert fig is not None
        assert ax is not None
        plt.close(fig)

    def test_matplotlib_plotting(self):
        """Test basic matplotlib plotting"""
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 2, 3])
        assert len(ax.lines) == 1
        plt.close(fig)


class TestFastAPIFunctionality:
    """Validate FastAPI core functionality"""

    def test_fastapi_app_creation(self):
        """Test FastAPI app instantiation"""
        from fastapi import FastAPI
        app = FastAPI()
        assert app is not None
        assert hasattr(app, "get")
        assert hasattr(app, "post")

    def test_fastapi_route_decorator(self):
        """Test FastAPI route decorator"""
        from fastapi import FastAPI

        app = FastAPI()

        @app.get("/test")
        def test_route():
            return {"message": "ok"}

        assert len(app.routes) > 0

    def test_pydantic_basemodel(self):
        """Test Pydantic v2 BaseModel"""
        from pydantic import BaseModel

        class Item(BaseModel):
            name: str
            price: float

        item = Item(name="Test", price=9.99)
        assert item.name == "Test"
        assert item.price == 9.99


class TestPytestIntegration:
    """Validate pytest framework functionality"""

    def test_pytest_version(self):
        """Test pytest is properly installed"""
        assert pytest.__version__ is not None
        v = version.parse(pytest.__version__)
        assert v >= version.parse("7.0.0")

    def test_pytest_fixtures(self):
        """Test pytest fixture functionality"""

        @pytest.fixture
        def sample_data():
            return [1, 2, 3, 4, 5]

        def test_with_fixture(sample_data):
            assert len(sample_data) == 5
            assert sum(sample_data) == 15

        test_with_fixture([1, 2, 3, 4, 5])


class TestPythonVersion:
    """Verify Python version compatibility"""

    def test_python_version_minimum(self):
        """Verify Python 3.10+ is running"""
        major, minor = sys.version_info[:2]
        assert (
            major > 3 or (major == 3 and minor >= 10)
        ), f"Python 3.10+ required, got {major}.{minor}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
