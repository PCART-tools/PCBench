from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.datasets import load_boston
(X, y) = load_boston(return_X_y=True)
est = HistGradientBoostingRegressor('least_squares',  0.1,  100,  31,  None,  20,  0.0, max_bins=255, warm_start=False, scoring=None, validation_fraction=0.1, n_iter_no_change=10, tol=1e-07, verbose=0, random_state=None)
