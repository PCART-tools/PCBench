import numpy as np
data = np.loadtxt('data.txt',  float, comments='#', delimiter=',', converters=None, skiprows=2, usecols=(0, 1), unpack=True, ndmin=2)
