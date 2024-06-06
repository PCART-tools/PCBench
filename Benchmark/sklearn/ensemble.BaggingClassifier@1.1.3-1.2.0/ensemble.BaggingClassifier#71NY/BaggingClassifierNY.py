from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
(X, y) = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = BaggingClassifier(SVC(),  10, bootstrap=True, oob_score=False, max_features=1.0, warm_start=False, bootstrap_features=False, n_jobs=None, max_samples=1.0, random_state=None).fit(X, y)
