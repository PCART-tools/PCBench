import pandas as pd
s = pd.Series(range(5))
s.where(other=False, axis=None, cond=s > 0)
