from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True,  False,  True,  False,  False,  True,  True, atol=1e-08, obj='Series', check_freq=True, rtol=1e-05, check_like=False, check_flags=True, check_index=True)
