import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(level=None, cond=s > 0, axis=None, other=np.nan, inplace=False, try_cast=False, errors='raise')
