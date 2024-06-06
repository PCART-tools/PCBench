import pandas as pd
s = pd.Series(range(5))
s.where(other=False, axis=None, inplace=False, cond=s > 0)
