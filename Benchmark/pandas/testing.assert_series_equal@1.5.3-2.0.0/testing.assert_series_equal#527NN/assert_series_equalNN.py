from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_series_type=True, atol=1e-08, check_categorical=True, check_freq=True, check_flags=True, check_like=False, check_names=True, check_dtype=True, rtol=1e-05, check_datetimelike_compat=False, check_category_order=True, check_less_precise=False, right=b, check_index_type='equiv', check_exact=False)
