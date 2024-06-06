from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(n_jobs=None, batch_size=3, shuffle=True, n_components=2, n_iter=100, method='lars', dict_init=None, verbose=False, iter_offset=0, callback=None, return_code=True, X=X, alpha=1)
