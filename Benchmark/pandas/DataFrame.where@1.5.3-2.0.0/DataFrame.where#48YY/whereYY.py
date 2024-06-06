import pandas as pd
s = pd.Series(range(5))
s.where(inplace=False, axis=None, cond=s > 0, other=False, level=None)
