from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X, n_iter=100, return_code=True, iter_offset=0, batch_size=3, shuffle=True, dict_init=None, callback=None, n_jobs=None, method='lars', n_components=2, verbose=False, alpha=1)
