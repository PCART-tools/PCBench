from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X,  2, dict_init=None, verbose=False, batch_size=3, n_iter=100, return_code=True, callback=None, alpha=1)
