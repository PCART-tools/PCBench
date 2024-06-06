import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.transforms import Bbox
import numpy as np
bbox = Bbox.from_bounds(0.1, 0.1, 0.8, 0.8)
bbox_image = mpimg.BboxImage(bbox,  'viridis',  None,  'bilinear',  'upper',  1,  4.0)
