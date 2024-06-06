from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(dict_init=None, alpha=1, batch_size=3, return_code=True, callback=None, X=X, n_iter=100)
