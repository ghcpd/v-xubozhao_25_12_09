#!/usr/bin/env python3

def main():
    print("Running demo...")

    try:
        import numpy as np
        # NumPy demo
        arr = np.random.rand(5)
        print(f"NumPy array: {arr}")
    except ImportError:
        print("NumPy not available")

    try:
        import pandas as pd
        # Pandas demo
        df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
        print(f"Pandas DataFrame:\n{df}")
    except ImportError:
        print("Pandas not available")

    try:
        from sklearn.linear_model import LinearRegression
        # Scikit-learn demo
        X = [[1], [2], [3]]
        y = [2, 4, 6]
        model = LinearRegression()
        model.fit(X, y)
        pred = model.predict([[4]])
        print(f"Scikit-learn prediction: {pred}")
    except ImportError:
        print("Scikit-learn not available")

    try:
        import matplotlib.pyplot as plt
        # Matplotlib demo (save plot)
        plt.plot([1, 2, 3], [1, 4, 2])
        plt.savefig('demo_plot.png')
        print("Matplotlib plot saved as demo_plot.png")
    except ImportError:
        print("Matplotlib not available")

    try:
        from scipy import stats
        # SciPy demo
        t_stat, p_val = stats.ttest_ind([1, 2, 3], [4, 5, 6])
        print(f"SciPy t-test: t={t_stat}, p={p_val}")
    except ImportError:
        print("SciPy not available")

    try:
        from fastapi import FastAPI
        # FastAPI demo
        app = FastAPI(title="Demo App")
        print(f"FastAPI app title: {app.title}")
    except ImportError:
        print("FastAPI not available")

    print("Demo completed successfully!")

if __name__ == "__main__":
    main()