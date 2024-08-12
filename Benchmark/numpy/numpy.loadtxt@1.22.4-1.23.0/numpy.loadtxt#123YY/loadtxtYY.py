import numpy as np
data = np.loadtxt('data.txt',  float,  '#',  ',',  None,  2, usecols=(0, 1), unpack=True, ndmin=2, encoding='utf-8', max_rows=100)
