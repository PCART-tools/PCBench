import numpy as np
from io import StringIO
with open('data2.txt', 'rb') as f:
    data = np.genfromtxt(f,  float,  '#', delimiter=',', skiprows=0, skip_header=0)
