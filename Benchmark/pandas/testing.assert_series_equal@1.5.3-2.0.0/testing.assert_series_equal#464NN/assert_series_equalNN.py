from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_category_order=True, check_index_type='equiv', check_index=True, check_series_type=True, check_exact=False, check_less_precise=False, check_freq=True, check_names=True, check_dtype=True, check_datetimelike_compat=False, rtol=1e-05, check_like=False, right=b, check_categorical=True, check_flags=True)
