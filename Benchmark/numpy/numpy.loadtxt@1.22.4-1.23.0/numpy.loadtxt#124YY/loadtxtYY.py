import numpy as np
data = np.loadtxt('data.txt',  float,  '#',  ',',  None,  2, ndmin=2, usecols=(0, 1), max_rows=100, like=None, unpack=True, encoding='utf-8')
