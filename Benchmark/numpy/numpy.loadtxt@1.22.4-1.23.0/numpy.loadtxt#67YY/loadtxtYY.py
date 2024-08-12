import numpy as np
data = np.loadtxt('data.txt', dtype=float, comments='#', delimiter=',', converters=None, skiprows=2, usecols=(0, 1), unpack=True)
