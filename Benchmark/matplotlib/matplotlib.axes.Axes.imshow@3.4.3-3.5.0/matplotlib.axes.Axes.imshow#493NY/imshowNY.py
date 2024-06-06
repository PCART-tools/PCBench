import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X,  'viridis',  None,  'auto', interpolation='nearest', origin='upper', vmax=None, filterrad=4.0, vmin=None, alpha=None)
