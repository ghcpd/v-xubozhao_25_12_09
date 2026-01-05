import importlib
import sys

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from fastapi import FastAPI


def test_imports():
    # Basic imports should succeed
    importlib.import_module('numpy')
    importlib.import_module('pandas')
    importlib.import_module('sklearn')
    importlib.import_module('fastapi')
    importlib.import_module('uvicorn')


def test_numpy_basic():
    a = np.array([1, 2, 3], dtype=float)
    assert a.mean() == 2.0


def test_pandas_basic():
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert df['a'].sum() == 6


def test_sklearn_small_train():
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    clf = RandomForestClassifier(n_estimators=5, random_state=42)
    clf.fit(X, y)
    preds = clf.predict(X)
    # at least better than random for sanity
    acc = (preds == y).mean()
    assert acc >= 0.5


def test_fastapi_app():
    app = FastAPI()
    assert hasattr(app, 'router')
