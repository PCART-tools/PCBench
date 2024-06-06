import pandas as pd
s = pd.Series(range(5))
s.where(s > 0, inplace=False, other=False)
