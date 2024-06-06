import pandas as pd
s = pd.Series(range(5))
s.where(s > 0,  False, inplace=False, errors='raise', level=None, axis=None)
