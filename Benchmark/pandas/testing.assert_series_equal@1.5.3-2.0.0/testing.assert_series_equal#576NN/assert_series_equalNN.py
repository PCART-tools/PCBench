from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True,  False, rtol=1e-05, check_flags=True, check_index=True, check_like=False, check_exact=False, check_datetimelike_compat=False, atol=1e-08, check_category_order=True, check_names=True, check_freq=True, obj='Series', check_categorical=True)
