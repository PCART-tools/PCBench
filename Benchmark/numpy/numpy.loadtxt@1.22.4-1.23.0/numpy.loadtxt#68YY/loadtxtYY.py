import numpy as np
data = np.loadtxt('data.txt', skiprows=2, dtype=float, usecols=(0, 1), converters=None, like=None, unpack=True, comments='#', delimiter=',')
