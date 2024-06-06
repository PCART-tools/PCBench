from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True,  False,  True,  False,  False, obj='Series', check_freq=True, check_category_order=True, atol=1e-08, check_categorical=True, check_like=False, rtol=1e-05, check_flags=True)
