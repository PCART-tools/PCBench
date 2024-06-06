import numpy as np
m = np.array([[1, 2], [3, 4], [5, 6]])
rotated_m = np.rot90(m, k=1)
print(rotated_m)
