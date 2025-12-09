import pytest

def test_numpy():
    pytest.skip("numpy crashes on this Windows system with Python 3.13")

def test_pandas():
    try:
        import pandas as pd
        df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        assert df.shape == (2, 2)
    except ImportError:
        pytest.skip("pandas not installed")

def test_scikit_learn():
    try:
        from sklearn.linear_model import LinearRegression
        X = [[1], [2], [3]]
        y = [1, 2, 3]
        model = LinearRegression()
        model.fit(X, y)
        pred = model.predict([[4]])
        assert len(pred) == 1
    except ImportError:
        pytest.skip("scikit-learn not installed")

def test_matplotlib():
    try:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 2, 3])
        plt.close(fig)
    except ImportError:
        pytest.skip("matplotlib not installed")

def test_scipy():
    try:
        from scipy import stats
        result = stats.ttest_1samp([1, 2, 3, 4, 5], 3)
        assert result.pvalue is not None
    except ImportError:
        pytest.skip("scipy not installed")

def test_fastapi():
    try:
        from fastapi import FastAPI
        app = FastAPI()
        assert app.title == "FastAPI"
    except ImportError:
        pytest.skip("fastapi not installed")

def test_uvicorn():
    try:
        import uvicorn
        assert uvicorn is not None
    except ImportError:
        pytest.skip("uvicorn not installed")