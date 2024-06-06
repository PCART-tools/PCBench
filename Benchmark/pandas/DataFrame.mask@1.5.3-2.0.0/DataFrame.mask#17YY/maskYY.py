import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(axis=None, cond=s > 0, inplace=False)
