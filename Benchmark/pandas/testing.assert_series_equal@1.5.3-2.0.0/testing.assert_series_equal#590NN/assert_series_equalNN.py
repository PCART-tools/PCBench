from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a,  b, check_less_precise=False, check_datetimelike_compat=False, check_flags=True, check_index=True, check_dtype=True, obj='Series', check_freq=True, check_category_order=True, atol=1e-08, check_series_type=True, check_index_type='equiv', rtol=1e-05, check_names=True, check_categorical=True, check_exact=False)
