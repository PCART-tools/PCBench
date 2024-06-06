import pandas as pd
s = pd.Series(range(5))
s.where(cond=s > 0, axis=None, inplace=False, level=None, errors='raise')
