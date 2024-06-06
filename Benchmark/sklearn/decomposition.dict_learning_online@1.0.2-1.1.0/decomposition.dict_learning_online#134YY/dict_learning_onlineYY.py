from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_components=2, verbose=False, return_code=True, callback=None, alpha=1, batch_size=3, shuffle=True, n_iter=100, dict_init=None)
