import pandas as pd
s = pd.Series(range(5))
s.where(inplace=False, other=False, cond=s > 0)
