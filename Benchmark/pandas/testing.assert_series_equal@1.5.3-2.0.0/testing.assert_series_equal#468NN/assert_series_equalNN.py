from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_index=True, check_exact=False, rtol=1e-05, left=a, check_freq=True, check_flags=True, check_less_precise=False, check_datetimelike_compat=False, check_index_type='equiv', check_like=False, check_category_order=True, check_names=True, check_categorical=True, right=b, check_series_type=True, check_dtype=True)
