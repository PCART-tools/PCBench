import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(s > 0, axis=None, errors='raise', level=None, inplace=False)
