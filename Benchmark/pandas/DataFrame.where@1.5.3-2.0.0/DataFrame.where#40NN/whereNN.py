import pandas as pd
s = pd.Series(range(5))
s.where(s > 0, axis=None, other=False, inplace=False, level=None, errors='raise', try_cast=False)
