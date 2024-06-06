from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_iter=100, batch_size=3, dict_init=None, callback=None, return_code=True, n_components=2, alpha=1)
