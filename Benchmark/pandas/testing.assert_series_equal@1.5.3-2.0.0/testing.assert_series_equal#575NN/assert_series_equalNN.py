from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True,  False, check_categorical=True, obj='Series', rtol=1e-05, check_names=True, check_like=False, check_freq=True, check_exact=False, check_flags=True, check_datetimelike_compat=False, atol=1e-08, check_category_order=True)
