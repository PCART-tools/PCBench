from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(right=b, check_exact=False, check_index_type='equiv', check_dtype=True, check_series_type=True, check_like=False, check_names=True, left=a, check_less_precise=False)
