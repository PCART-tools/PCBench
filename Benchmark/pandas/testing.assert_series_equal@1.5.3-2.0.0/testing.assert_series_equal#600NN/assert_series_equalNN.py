from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(right=b, atol=1e-08, check_category_order=True, check_less_precise=False, check_freq=True, check_categorical=True, check_series_type=True, check_like=False, check_index=True, check_names=True, rtol=1e-05, check_flags=True, left=a, check_exact=False, check_dtype=True, check_datetimelike_compat=False, obj='Series', check_index_type='equiv')
