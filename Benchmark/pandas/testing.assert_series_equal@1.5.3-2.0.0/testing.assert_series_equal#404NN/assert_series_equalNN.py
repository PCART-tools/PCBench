from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_index_type='equiv', check_flags=True, check_category_order=True, check_like=False, check_dtype=True, check_exact=False, check_categorical=True, right=b, check_less_precise=False, check_freq=True, check_index=True, check_names=True, check_datetimelike_compat=False, check_series_type=True)
