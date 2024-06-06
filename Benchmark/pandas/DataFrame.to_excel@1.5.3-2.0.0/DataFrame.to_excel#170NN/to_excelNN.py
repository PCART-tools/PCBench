import pandas as pd
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
df1.to_excel(excel_writer='output.xlsx', sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=False, inf_rep='inf', verbose=False, freeze_panes=None, storage_options=None)
