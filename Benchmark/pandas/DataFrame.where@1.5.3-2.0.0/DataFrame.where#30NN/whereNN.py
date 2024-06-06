import pandas as pd
s = pd.Series(range(5))
s.where(s > 0,  False, try_cast=False, level=None, axis=None, errors='raise', inplace=False)
