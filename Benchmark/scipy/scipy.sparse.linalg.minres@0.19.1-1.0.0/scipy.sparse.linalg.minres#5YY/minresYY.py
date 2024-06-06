import numpy as np
from scipy.sparse.linalg import minres
A = np.array([[4.0, 1.0], [1.0, 3.0]], dtype=float)
b = np.array([1.0, 2.0], dtype=float)
x0 = np.array([0.0, 0.0], dtype=float)
(x, info) = minres(A,  b, x0=x0)
