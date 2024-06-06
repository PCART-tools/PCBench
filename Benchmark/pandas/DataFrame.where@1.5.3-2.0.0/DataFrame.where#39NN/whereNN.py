import pandas as pd
s = pd.Series(range(5))
s.where(s > 0, axis=None, errors='raise', level=None, other=False, inplace=False)
