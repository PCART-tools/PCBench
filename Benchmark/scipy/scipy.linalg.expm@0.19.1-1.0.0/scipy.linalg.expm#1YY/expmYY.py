import numpy as np
from scipy.linalg import expm
A = np.array([[1, 2], [3, 4]])
result = expm(A)
