import numpy as np
sample = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = np.histogramdd(sample, bins=10, range=None, normed=None, weights=None, density=None)
