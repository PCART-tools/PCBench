import numpy as np
data = np.loadtxt('data.txt',  float,  '#',  ',',  None, unpack=True, skiprows=2, like=None, usecols=(0, 1))
