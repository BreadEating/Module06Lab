from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
import joblib
import os
iris = load_iris()
X, y = iris.data, iris.target
clf = GaussianNB()
clf.fit(X, y)

folder_name = "artifacts"
os.makedirs(folder_name, exist_ok=True)

joblib.dump(clf, os.path.join(folder_name, "model.pkl"))