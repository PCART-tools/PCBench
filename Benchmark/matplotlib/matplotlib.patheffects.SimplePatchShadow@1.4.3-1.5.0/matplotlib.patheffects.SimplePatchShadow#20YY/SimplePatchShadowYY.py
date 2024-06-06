import matplotlib
matplotlib.use('Agg')
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
pe_shadow = pe.SimplePatchShadow((3, -3), shadow_rgbFace='gray', alpha=None, patch_alpha=0.2, rho=0.5)
