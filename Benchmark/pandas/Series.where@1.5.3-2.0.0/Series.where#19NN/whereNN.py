import pandas as pd
s = pd.Series(range(5))
s.where(axis=None, level=None, inplace=False, cond=s > 0, errors='raise')
