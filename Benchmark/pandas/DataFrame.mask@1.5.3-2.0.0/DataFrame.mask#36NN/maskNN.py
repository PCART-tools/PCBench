import pandas as pd
import numpy as np
s = pd.Series(range(5))
s.mask(s > 0, try_cast=False, other=np.nan)
