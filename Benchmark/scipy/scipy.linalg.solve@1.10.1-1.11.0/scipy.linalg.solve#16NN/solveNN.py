import scipy.linalg
a = [[2, 1], [5, 3]]
b = [1, 2]
x = scipy.linalg.solve(a,  b, sym_pos=False, lower=False, overwrite_a=False)
