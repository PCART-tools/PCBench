import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto',  'nearest', resample=None, filternorm=True, vmax=None, vmin=None, filterrad=4.0, alpha=None, origin='upper')
