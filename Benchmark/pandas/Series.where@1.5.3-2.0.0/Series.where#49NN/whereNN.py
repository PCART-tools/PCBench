import pandas as pd
s = pd.Series(range(5))
s.where(cond=s > 0, axis=None, level=None, errors='raise', inplace=False, other=False)
