from sklearn.decomposition import dict_learning_online
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
dict_learning_online(X,  2, alpha=1, n_iter=100, callback=None, batch_size=3, dict_init=None, return_code=True)
