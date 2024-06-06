import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(other=np.nan, level=None, errors='raise', axis=None, inplace=False, cond=s > 0)
