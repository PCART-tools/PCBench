import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(np.nan,  'mean',  None, verbose=0, copy=True)
