import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto',  'nearest',  None, vmin=None, filternorm=True, vmax=None, origin='upper', filterrad=4.0, extent=None, resample=None)
