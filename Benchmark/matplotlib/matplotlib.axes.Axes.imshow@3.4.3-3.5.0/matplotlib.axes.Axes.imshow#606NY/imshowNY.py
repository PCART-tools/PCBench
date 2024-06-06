import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto', interpolation='nearest', extent=None, origin='upper', vmin=None, data=None, alpha=None, vmax=None)
