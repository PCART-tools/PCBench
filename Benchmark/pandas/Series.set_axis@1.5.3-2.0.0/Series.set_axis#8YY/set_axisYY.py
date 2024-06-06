import pandas as pd
s = pd.Series([1, 2, 3])
s.set_axis(axis=0, labels=['a', 'b', 'c'])
