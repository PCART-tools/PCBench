from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b, check_datetimelike_compat=False, atol=1e-08, check_flags=True, check_index_type='equiv', check_freq=True, check_categorical=True, check_dtype=True, check_names=True, check_series_type=True, check_like=False, check_less_precise=False, rtol=1e-05, check_exact=False, check_category_order=True)
