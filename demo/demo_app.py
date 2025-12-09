"""Tiny demo module used by tests to validate that core libraries import and run.

This file implements a couple of tiny helper functions that use numpy, pandas and scikit-learn
so tests can confirm those libraries are functioning as expected.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression


def create_linear_dataset(n=20):
    rng = np.random.RandomState(0)
    X = 2.0 * rng.rand(n, 1)
    y = 4.0 + 3.0 * X[:, 0] + rng.randn(n)
    return X.reshape(-1, 1), y


def fit_linear_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model


def dataframe_from_numpy(X, y):
    return pd.DataFrame({"X": X.flatten(), "y": y})
