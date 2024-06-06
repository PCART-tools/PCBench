import pandas as pd
s = pd.Series(range(5))
s.where(s > 0, level=None, other=False, inplace=False, errors='raise', axis=None)
