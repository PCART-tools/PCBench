import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(level=None, inplace=False, try_cast=False, axis=None, cond=s > 0, errors='raise')
