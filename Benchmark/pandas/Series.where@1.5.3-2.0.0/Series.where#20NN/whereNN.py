import pandas as pd
s = pd.Series(range(5))
s.where(axis=None, cond=s > 0, try_cast=False, inplace=False, level=None, errors='raise')
