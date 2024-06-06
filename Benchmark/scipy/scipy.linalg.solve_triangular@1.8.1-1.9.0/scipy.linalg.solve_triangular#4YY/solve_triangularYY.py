import numpy as np
from scipy.linalg import solve_triangular
a = np.array([[2, 0, 0], [1, 3, 0], [4, 5, 6]])
b = np.array([1, 2, 3])
x = solve_triangular(a,  b,  0)
