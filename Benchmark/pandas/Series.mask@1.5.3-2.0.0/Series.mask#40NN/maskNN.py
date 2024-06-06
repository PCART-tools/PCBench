import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(s > 0, level=None, other=np.nan, try_cast=False, axis=None, inplace=False, errors='raise')
