from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b,  True, check_less_precise=False, rtol=1e-05, check_categorical=True, check_datetimelike_compat=False, check_like=False, obj='Series', check_flags=True, atol=1e-08, check_freq=True, check_category_order=True, check_index_type='equiv', check_series_type=True, check_exact=False, check_names=True)
