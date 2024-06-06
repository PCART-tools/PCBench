import numpy as np
from scipy.linalg import solve_banded
l_and_u = (1, 1)
ab = np.array([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 0.0]])
b = np.array([1.0, 2.0, 3.0])
result = solve_banded(l_and_u=l_and_u, ab=ab, b=b, overwrite_ab=False, overwrite_b=False, debug=None)
print(result)
