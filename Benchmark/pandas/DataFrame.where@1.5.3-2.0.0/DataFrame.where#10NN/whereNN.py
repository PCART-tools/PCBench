import pandas as pd
s = pd.Series(range(5))
s.where(s > 0, errors='raise', level=None, axis=None, try_cast=False, inplace=False)
