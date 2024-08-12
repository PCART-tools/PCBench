import numpy as np
data = np.loadtxt('data.txt', like=None, skiprows=2, delimiter=',', comments='#', usecols=(0, 1), unpack=True, converters=None, ndmin=2, dtype=float)
