from scipy.sparse.linalg import qmr
import scipy.sparse as sp
A = sp.csc_matrix([[4, 2], [2, 3]])
b = [1, 2]
x0 = [0, 0]
result = qmr(A=A, b=b, x0=x0, tol=1e-05, maxiter=None, xtype=None, M1=None, M2=None, callback=None)
