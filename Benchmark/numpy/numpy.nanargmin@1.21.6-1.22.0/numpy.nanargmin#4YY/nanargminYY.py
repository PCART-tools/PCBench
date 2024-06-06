import numpy as np
a = np.array([[np.nan, 4, 2], [7, 5, 6]])
result = np.nanargmin(a, axis=0)
