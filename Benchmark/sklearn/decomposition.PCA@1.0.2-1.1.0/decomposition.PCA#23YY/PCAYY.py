import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(2, tol=0.0, copy=True, iterated_power='auto', svd_solver='auto', whiten=False)
