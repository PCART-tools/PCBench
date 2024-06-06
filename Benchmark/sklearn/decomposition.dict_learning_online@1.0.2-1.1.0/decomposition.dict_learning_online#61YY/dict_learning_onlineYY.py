from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(batch_size=3, dict_init=None, callback=None, return_code=True, alpha=1, X=X, verbose=False, n_iter=100)
