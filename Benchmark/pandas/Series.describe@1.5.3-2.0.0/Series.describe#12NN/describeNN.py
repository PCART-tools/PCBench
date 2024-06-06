import pandas as pd
s = pd.Series([1, 2, 3])
s.describe(None,  None,  None, datetime_is_numeric=False)
