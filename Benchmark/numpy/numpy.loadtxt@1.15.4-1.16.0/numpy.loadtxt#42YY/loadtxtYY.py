import numpy as np
data = np.loadtxt('./data.txt',  float,  '#', delimiter=',', converters=None, skiprows=1, usecols=(0, 2), unpack=True, ndmin=1)
