import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(other=np.nan, level=None, cond=s > 0)
