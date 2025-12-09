"""Minimal demo script that trains a tiny classifier and prints accuracy."""
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=200, n_features=10, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
clf = RandomForestClassifier(n_estimators=10, random_state=0)
clf.fit(X_train, y_train)
print(f"Demo accuracy: {clf.score(X_test, y_test):.3f}")
