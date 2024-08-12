import numpy as np
data = np.loadtxt('data.txt',  float,  '#',  ',', usecols=(0, 1), unpack=True, like=None, converters=None, ndmin=2, skiprows=2)
