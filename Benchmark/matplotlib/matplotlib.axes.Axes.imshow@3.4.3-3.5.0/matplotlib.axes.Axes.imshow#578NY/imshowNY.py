import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto',  'nearest',  None,  None, vmax=None, extent=None, filterrad=4.0, resample=None, filternorm=True, origin='upper')
