import numpy as np
x = np.random.randn(1000)
y = np.random.randn(1000)
(hist, x_edges, y_edges) = np.histogram2d(x,  y,  10,  [[-2, 2], [-2, 2]],  True,  x + y, density=None)
