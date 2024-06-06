import scipy.linalg
a = [[2, 1], [5, 3]]
b = [1, 2]
x = scipy.linalg.solve(a=a, b=b, sym_pos=False)
