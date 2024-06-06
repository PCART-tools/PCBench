import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto',  'nearest', filterrad=4.0, resample=None, alpha=None, vmax=None, url=None, vmin=None, filternorm=True)
