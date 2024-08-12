import numpy as np
data = np.loadtxt('data.txt',  float,  '#',  ',', converters=None, skiprows=1, usecols=(0, 2), unpack=True, ndmin=1, encoding='utf-8')
