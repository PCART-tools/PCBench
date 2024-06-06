from pandas import testing as tm
import pandas as pd
a = pd.Index([1, 2, 3])
b = pd.Index([1, 2, 3])
tm.assert_index_equal(left=a, right=b, exact='equiv', check_names=True)
