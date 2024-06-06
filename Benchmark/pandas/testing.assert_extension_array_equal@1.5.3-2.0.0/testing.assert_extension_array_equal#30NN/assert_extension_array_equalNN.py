from pandas import testing as tm
import pandas as pd
a = pd.Series([1, 2, 3, 4])
(b, c) = (a.array, a.array)
tm.assert_extension_array_equal(b,  c,  True, index_values=None, check_less_precise=False, check_exact=False, rtol=1e-05)
