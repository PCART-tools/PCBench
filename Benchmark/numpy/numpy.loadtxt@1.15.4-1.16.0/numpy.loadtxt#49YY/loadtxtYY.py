import numpy as np
data = np.loadtxt('./data.txt',  float,  '#',  ',',  None,  1,  (0, 2), unpack=True, ndmin=1, encoding='utf-8')
