import pandas as pd
s = pd.Series(range(5))
s.where(axis=None, errors='raise', try_cast=False, cond=s > 0, level=None, inplace=False)
