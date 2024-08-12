import numpy as np
data = np.loadtxt('data.txt',  float,  '#', unpack=True, converters=None, skiprows=2, delimiter=',', usecols=(0, 1), like=None)
