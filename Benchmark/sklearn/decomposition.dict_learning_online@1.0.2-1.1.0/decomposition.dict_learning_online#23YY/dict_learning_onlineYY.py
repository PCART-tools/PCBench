from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, dict_init=None, callback=None, n_iter=100, alpha=1, return_code=True)
