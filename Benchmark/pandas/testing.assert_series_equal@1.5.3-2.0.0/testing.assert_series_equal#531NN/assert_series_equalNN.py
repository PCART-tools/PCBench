from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_categorical=True, check_exact=False, check_less_precise=False, check_series_type=True, check_like=False, left=a, check_dtype=True, check_index_type='equiv', check_datetimelike_compat=False, right=b, rtol=1e-05, check_freq=True, atol=1e-08, check_flags=True, check_category_order=True, check_names=True)
