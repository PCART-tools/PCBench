import numpy as np
x = np.random.randn(1000)
y = np.random.randn(1000)
(hist, x_edges, y_edges) = np.histogram2d(x,  y, bins=10, range=[[-2, 2], [-2, 2]], normed=True, weights=x + y, density=None)
