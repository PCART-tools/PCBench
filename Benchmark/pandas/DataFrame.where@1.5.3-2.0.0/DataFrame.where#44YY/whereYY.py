import pandas as pd
s = pd.Series(range(5))
s.where(other=False, cond=s > 0, level=None)
