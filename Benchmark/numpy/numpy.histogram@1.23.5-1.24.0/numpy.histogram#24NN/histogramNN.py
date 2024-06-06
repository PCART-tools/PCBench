import numpy as np
a = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
bins = 4
range = (1, 5)
normed = False
weights = None
density = None
(hist, bin_edges) = np.histogram(a,  bins,  range, normed=normed, weights=weights, density=density)
