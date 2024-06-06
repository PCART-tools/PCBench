import pandas as pd
df = pd.DataFrame(dict(name=['Raphael', 'Donatello'], mask=['red', 'purple'], weapon=['sai', 'bo staff']))
print(df.to_latex(None,  None,  None,  True,  True,  'NaN',  None,  None,  None,  True,  False,  None,  None,  None, encoding=None, decimal='.', multicolumn=None, multicolumn_format=None, multirow=None))
