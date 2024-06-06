from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_datetimelike_compat=False, check_category_order=True, check_exact=False, check_flags=True, left=a, check_like=False, rtol=1e-05, check_less_precise=False, check_dtype=True, right=b, check_series_type=True, check_categorical=True, check_names=True, check_index_type='equiv', check_freq=True)
