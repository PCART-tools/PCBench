import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(axis=None, other=np.nan, cond=s > 0)
