import pandas as pd
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
df1.to_excel('./output.xlsx',  'Sheet1',  '',  None,  None,  True,  True,  None,  0,  0,  None,  True,  False, inf_rep='inf', verbose=False, freeze_panes=None, storage_options=None)
