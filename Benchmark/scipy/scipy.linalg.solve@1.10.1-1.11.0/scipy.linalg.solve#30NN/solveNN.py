import scipy.linalg
a = [[2, 1], [5, 3]]
b = [1, 2]
x = scipy.linalg.solve(a,  b,  False, lower=False, overwrite_a=False, overwrite_b=False, check_finite=True)
