import numpy as np
data = np.loadtxt('data.txt',  float,  '#',  ',',  None, encoding='utf-8', usecols=(0, 1), skiprows=2, unpack=True, ndmin=2, like=None)
