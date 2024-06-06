import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto', alpha=None, vmin=None, filternorm=True, interpolation='nearest', filterrad=4.0, resample=None)
