import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(cond=s > 0, inplace=False, other=np.nan, level=None, axis=None)
