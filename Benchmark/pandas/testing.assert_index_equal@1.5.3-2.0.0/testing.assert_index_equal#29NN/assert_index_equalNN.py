from pandas import testing as tm
import pandas as pd
a = pd.Index([1, 2, 3])
b = pd.Index([1, 2, 3])
tm.assert_index_equal(a,  b,  'equiv',  True, check_less_precise=False, check_exact=True, check_categorical=True)
