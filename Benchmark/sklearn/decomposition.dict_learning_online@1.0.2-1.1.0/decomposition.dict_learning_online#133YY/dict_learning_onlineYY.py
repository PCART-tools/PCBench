from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, return_code=True, n_components=2, verbose=False, dict_init=None, callback=None, n_iter=100, batch_size=3, alpha=1)
