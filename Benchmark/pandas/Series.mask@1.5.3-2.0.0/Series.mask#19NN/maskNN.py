import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(level=None, errors='raise', cond=s > 0, inplace=False, axis=None)
