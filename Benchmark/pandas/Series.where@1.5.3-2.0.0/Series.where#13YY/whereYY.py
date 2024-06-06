import pandas as pd
s = pd.Series(range(5))
s.where(axis=None, cond=s > 0)
