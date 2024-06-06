import pandas as pd
s = pd.Series(range(5))
s.where(inplace=False, axis=None, level=None, cond=s > 0)
