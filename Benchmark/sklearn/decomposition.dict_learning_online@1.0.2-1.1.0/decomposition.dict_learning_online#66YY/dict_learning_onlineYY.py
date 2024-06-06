from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(iter_offset=0, X=X, shuffle=True, random_state=None, dict_init=None, return_code=True, method='lars', batch_size=3, alpha=1, n_iter=100, n_jobs=None, callback=None, verbose=False)
