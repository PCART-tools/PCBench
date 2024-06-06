from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(a, check_like=False, check_index_type='equiv', check_names=True, check_series_type=True, check_dtype=True, right=b, check_less_precise=False, check_exact=False)
