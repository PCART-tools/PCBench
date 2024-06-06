from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv',  True, check_less_precise=False, atol=1e-08, check_datetimelike_compat=False, check_names=True, check_like=False, check_category_order=True, rtol=1e-05, check_flags=True, check_categorical=True, check_exact=False, check_index=True, check_freq=True)
