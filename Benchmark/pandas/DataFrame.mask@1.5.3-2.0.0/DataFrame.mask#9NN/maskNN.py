import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(s > 0, inplace=False, level=None, errors='raise', axis=None)
