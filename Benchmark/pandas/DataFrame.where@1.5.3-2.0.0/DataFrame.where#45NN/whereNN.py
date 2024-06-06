import pandas as pd
s = pd.Series(range(5))
s.where(errors='raise', cond=s > 0, other=False)
