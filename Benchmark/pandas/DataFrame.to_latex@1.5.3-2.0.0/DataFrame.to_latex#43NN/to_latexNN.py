import pandas as pd
df = pd.DataFrame(dict(name=['Raphael', 'Donatello'], mask=['red', 'purple'], weapon=['sai', 'bo staff']))
print(df.to_latex(None,  None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None))
