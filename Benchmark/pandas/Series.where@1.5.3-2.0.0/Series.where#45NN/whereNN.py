import pandas as pd
s = pd.Series(range(5))
s.where(other=False, errors='raise', cond=s > 0)
