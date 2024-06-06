import pandas as pd
s = pd.Series(range(5))
s.where(s > 0, level=None, inplace=False, axis=None, errors='raise', try_cast=False)
