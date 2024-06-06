from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_index_type='equiv', check_names=True, check_series_type=True, check_dtype=True, right=b, atol=1e-08, rtol=1e-05, check_freq=True, check_index=True, check_datetimelike_compat=False, check_categorical=True, check_exact=False, check_less_precise=False, check_category_order=True, check_flags=True, obj='Series')
