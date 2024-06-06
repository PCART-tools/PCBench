from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b, atol=1e-08, check_flags=True, check_like=False, check_less_precise=False, check_names=True, check_dtype=True, rtol=1e-05, check_freq=True, check_exact=False, check_datetimelike_compat=False, check_series_type=True, check_index_type='equiv', check_category_order=True, obj='Series', check_categorical=True, check_index=True)
