from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True,  'equiv', check_exact=False, atol=1e-08, check_flags=True, rtol=1e-05, check_series_type=True, check_like=False, check_datetimelike_compat=False, check_index=True, check_less_precise=False, check_categorical=True, check_names=True, check_category_order=True, check_freq=True)
