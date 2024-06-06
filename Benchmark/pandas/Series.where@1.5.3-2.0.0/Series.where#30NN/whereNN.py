import pandas as pd
s = pd.Series(range(5))
s.where(s > 0,  False, axis=None, inplace=False, level=None, try_cast=False, errors='raise')
