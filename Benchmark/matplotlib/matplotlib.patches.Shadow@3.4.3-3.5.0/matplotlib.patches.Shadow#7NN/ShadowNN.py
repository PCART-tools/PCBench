import matplotlib.patches as patches
patch = patches.Rectangle((0, 0), 1, 1)
shadow = patches.Shadow(patch,  0.1, oy=0.1, props=None)
