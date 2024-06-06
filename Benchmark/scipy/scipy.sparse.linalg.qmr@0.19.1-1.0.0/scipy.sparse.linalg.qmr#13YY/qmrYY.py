from scipy.sparse.linalg import qmr
import scipy.sparse as sp
A = sp.csc_matrix([[4, 2], [2, 3]])
b = [1, 2]
x0 = [0, 0]
result = qmr(A,  b,  x0,  1e-05,  None)
