import numpy as np
data = np.genfromtxt('./data.csv',  float, comments='#', delimiter=',', skip_header=0, skip_footer=0, converters=None)
