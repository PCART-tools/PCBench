import pandas as pd
s = pd.Series(range(5))
s.where(axis=None, inplace=False, level=None, cond=s > 0)
