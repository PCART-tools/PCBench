import pandas as pd
idx = pd.Index(list('abcd'))
idx.slice_locs(start='b', end='c')
