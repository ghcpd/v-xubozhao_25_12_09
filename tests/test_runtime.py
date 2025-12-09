import numpy as np
import pandas as pd
import pytest

sklearn = pytest.importorskip("sklearn", reason="sklearn not installed (wheel/build tools missing)")
from sklearn.tree import DecisionTreeClassifier
from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_numpy_sum():
    a = np.array([1, 2, 3])
    assert a.sum() == 6


def test_pandas_operations():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert df["a"].sum() == 6
    assert df.shape == (3, 2)


def test_sklearn_fit_predict():
    X = [[0, 0], [1, 1], [1, 0], [0, 1]]
    y = [0, 1, 1, 0]
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X, y)
    preds = clf.predict([[0, 0], [1, 1]])
    assert list(preds) == [0, 1]


def test_fastapi_app_simple():
    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"ping": "pong"}

    client = TestClient(app)
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json() == {"ping": "pong"}
