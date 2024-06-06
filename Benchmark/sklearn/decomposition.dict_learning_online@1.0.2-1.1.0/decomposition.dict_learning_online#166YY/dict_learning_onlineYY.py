from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X=X, dict_init=None, n_components=2, alpha=1, return_code=True, n_iter=100)
