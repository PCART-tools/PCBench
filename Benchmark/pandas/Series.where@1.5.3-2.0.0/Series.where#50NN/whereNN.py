import pandas as pd
s = pd.Series(range(5))
s.where(try_cast=False, other=False, level=None, errors='raise', axis=None, inplace=False, cond=s > 0)
