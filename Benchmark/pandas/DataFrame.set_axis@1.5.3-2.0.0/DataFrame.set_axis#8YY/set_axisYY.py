import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.set_axis(axis='index', labels=['a', 'b', 'c'])
