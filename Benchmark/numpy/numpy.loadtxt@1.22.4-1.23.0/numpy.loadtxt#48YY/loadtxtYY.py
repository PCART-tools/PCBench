import numpy as np
data = np.loadtxt('data.txt',  float, delimiter=',', skiprows=2, comments='#', usecols=(0, 1), like=None, converters=None)
