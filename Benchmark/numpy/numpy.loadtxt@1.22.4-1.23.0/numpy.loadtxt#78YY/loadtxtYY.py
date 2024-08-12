import numpy as np
data = np.loadtxt('data.txt',  float,  '#',  ',',  None,  2, unpack=True, usecols=(0, 1), like=None, ndmin=2)
