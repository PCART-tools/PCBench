import numpy as np
from io import StringIO
with open('./data2.txt', 'rb') as f:
    data = np.genfromtxt(fname=f, dtype=float, comments='#', delimiter=',', skiprows=0, skip_header=0, skip_footer=0)
