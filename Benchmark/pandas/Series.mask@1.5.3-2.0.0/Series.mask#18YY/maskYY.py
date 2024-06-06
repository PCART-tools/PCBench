import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(level=None, axis=None, inplace=False, cond=s > 0)
