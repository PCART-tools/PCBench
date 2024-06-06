import matplotlib
matplotlib.use('Agg')
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
pe_shadow = pe.SimplePatchShadow(offset=(3, -3), shadow_rgbFace='gray', alpha=None)
