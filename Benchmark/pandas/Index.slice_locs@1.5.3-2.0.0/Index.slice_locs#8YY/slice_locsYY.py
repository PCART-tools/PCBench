import pandas as pd
idx = pd.Index(list('abcd'))
idx.slice_locs('b',  'c', step=None)
