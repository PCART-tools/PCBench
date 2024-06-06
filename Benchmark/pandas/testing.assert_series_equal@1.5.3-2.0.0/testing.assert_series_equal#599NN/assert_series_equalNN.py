from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(check_index_type='equiv', check_exact=False, check_category_order=True, obj='Series', right=b, check_freq=True, check_less_precise=False, check_datetimelike_compat=False, check_names=True, left=a, check_series_type=True, check_flags=True, check_categorical=True, rtol=1e-05, check_like=False, atol=1e-08, check_dtype=True)
