from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
(b, c) = (a.array, a.array)
tm.assert_extension_array_equal(b, right=c, check_dtype=True, index_values=None, check_less_precise=False)
