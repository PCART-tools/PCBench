import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(s > 0, axis=None, level=None, inplace=False, try_cast=False, errors='raise')
