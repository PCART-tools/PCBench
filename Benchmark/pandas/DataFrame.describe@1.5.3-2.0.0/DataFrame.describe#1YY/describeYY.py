import pandas as pd
df = pd.DataFrame({'categorical': pd.Categorical(['d', 'e', 'f']), 'numeric': [1, 2, 3], 'object': ['a', 'b', 'c']})
df.describe()
