import pandas as pd
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
df1.to_excel('./output.xlsx',  'Sheet1', na_rep='', float_format=None, columns=None, header=True)
