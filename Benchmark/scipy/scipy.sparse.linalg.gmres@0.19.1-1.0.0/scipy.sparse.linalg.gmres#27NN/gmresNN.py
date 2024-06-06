import numpy as np
from scipy.sparse.linalg import gmres
A = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]], dtype=float)
b = np.array([1, 1, 1], dtype=float)
x0 = None
tol = 1e-05
restart = None
maxiter = None
xtype = None
M = None
callback = None
restrt = None
(x, info) = gmres(A,  b,  x0,  tol,  restart,  maxiter, xtype=xtype)
print('Solution:', x)
print('Info:', info)
