from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, rtol=1e-05, right=b, atol=1e-08, check_flags=True, check_exact=False, check_series_type=True, check_datetimelike_compat=False, check_names=True, check_like=False, check_category_order=True, check_dtype=True, check_index_type='equiv', check_freq=True, obj='Series', check_less_precise=False, check_categorical=True)
