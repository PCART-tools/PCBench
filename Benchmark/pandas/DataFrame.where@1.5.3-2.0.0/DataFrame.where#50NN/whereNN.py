import pandas as pd
s = pd.Series(range(5))
s.where(try_cast=False, inplace=False, cond=s > 0, other=False, errors='raise', level=None, axis=None)
