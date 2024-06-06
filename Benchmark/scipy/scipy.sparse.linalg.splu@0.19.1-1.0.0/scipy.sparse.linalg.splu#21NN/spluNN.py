from scipy.sparse import csc_matrix
from scipy.sparse.linalg import splu
A = csc_matrix([[1, 2, 0], [3, 4, 0], [0, 5, 6]])
lu = splu(A,  'MMD_AT_PLUS_A',  0.1,  0.2,  1.0,  10)
