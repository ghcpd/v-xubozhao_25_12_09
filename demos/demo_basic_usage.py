"""Minimal demo script exercising key libraries.

This is not a production server — just a tiny runtime check you can run manually.
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def demo():
    print('numpy version:', np.__version__)
    print('pandas version:', pd.__version__)

    # small data transformation
    a = np.arange(4)[:, None] + 1
    y = (a * 2).ravel()
    print('X:', a.ravel(), 'y:', y)

    df = pd.DataFrame({'X': a.ravel(), 'y': y})
    print('DataFrame head:\n', df.head())

    model = LinearRegression()
    model.fit(a, y)
    print('Simple regression coef, intercept:', model.coef_, model.intercept_)


if __name__ == '__main__':
    demo()
