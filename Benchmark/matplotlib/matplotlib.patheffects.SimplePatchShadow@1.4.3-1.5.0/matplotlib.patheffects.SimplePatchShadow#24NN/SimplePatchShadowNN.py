import matplotlib
matplotlib.use('Agg')
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
pe_shadow = pe.SimplePatchShadow((3, -3),  'gray',  None,  0.2, rho=0.5, offset_xy=None)
