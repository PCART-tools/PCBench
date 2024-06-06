import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto', filternorm=True, vmin=None, vmax=None, interpolation='nearest', resample=None, alpha=None, filterrad=4.0)
