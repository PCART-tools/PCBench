import numpy as np
data = np.loadtxt('data.txt',  float,  '#',  ',',  None, skiprows=2, ndmin=2, max_rows=100, like=None, encoding='utf-8', usecols=(0, 1), unpack=True)
