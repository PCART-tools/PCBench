import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(other=np.nan, cond=s > 0, axis=None, inplace=False, errors='raise', level=None)
