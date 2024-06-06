from scipy.sparse.linalg import bicgstab
import numpy as np
A = np.array([[1.0, 2.0], [2.0, 3.0]])
b = np.array([1.0, 2.0])
x0 = np.array([0.0, 0.0])
tol = 1e-05
maxiter = 100
(x, info) = bicgstab(A,  b,  x0,  tol,  maxiter, xtype=None, M=None)
