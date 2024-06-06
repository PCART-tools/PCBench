import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(try_cast=False, cond=s > 0)
