from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(shuffle=True, callback=None, alpha=1, verbose=False, n_components=2, batch_size=3, n_jobs=None, X=X, return_code=True, dict_init=None, n_iter=100, method='lars')
