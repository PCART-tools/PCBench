from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X,  2, shuffle=True, verbose=False, callback=None, n_jobs=None, return_code=True, alpha=1, dict_init=None, n_iter=100, batch_size=3)
