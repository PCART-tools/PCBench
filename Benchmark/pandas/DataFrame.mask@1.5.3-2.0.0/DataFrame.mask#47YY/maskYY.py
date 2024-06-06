import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(inplace=False, axis=None, cond=s > 0, other=np.nan)
