import pandas as pd
s = pd.Series(range(5))
s.where(level=None, other=False, cond=s > 0)
