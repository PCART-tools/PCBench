from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
b = pd.Series([1, 2, 3, 4])
tm.assert_series_equal(right=b, left=a, check_index_type='equiv', check_series_type=True, check_like=False, check_index=True, check_dtype=True)
