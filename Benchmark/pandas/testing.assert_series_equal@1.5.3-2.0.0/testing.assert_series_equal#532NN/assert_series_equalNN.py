from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_category_order=True, rtol=1e-05, check_index=True, atol=1e-08, check_exact=False, check_datetimelike_compat=False, right=b, check_like=False, check_series_type=True, left=a, check_names=True, check_flags=True, check_categorical=True, check_less_precise=False, check_index_type='equiv', check_dtype=True, check_freq=True)
