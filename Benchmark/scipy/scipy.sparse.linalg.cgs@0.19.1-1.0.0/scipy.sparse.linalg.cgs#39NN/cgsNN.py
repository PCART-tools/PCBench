from scipy.sparse.linalg import cgs
from scipy.sparse import csc_matrix
import numpy as np
A = csc_matrix([[3, 2], [2, 3]])
b = np.array([2, -1])
(x, info) = cgs(A,  b,  None, tol=1e-05, maxiter=100, xtype=None, M=None, callback=None)
