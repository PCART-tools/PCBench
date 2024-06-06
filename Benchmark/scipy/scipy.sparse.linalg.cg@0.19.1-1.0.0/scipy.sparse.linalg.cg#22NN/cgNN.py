from scipy.sparse.linalg import cg
import scipy.sparse as sp
A = sp.csr_matrix([[3, 2], [2, 3]])
b = [2, 2]
(x, info) = cg(A,  b,  None, tol=1e-05, maxiter=None, xtype=None)
