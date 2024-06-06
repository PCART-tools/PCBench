import pandas as pd
s = pd.Series(range(5))
s.where(inplace=False, cond=s > 0, other=False, axis=None, level=None)
