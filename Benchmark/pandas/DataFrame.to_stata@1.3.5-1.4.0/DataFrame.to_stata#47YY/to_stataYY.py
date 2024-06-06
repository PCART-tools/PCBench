import pandas as pd
df = pd.DataFrame({'animal': ['falcon', 'parrot', 'falcon', 'parrot'], 'speed': [350, 18, 361, 15]})
df.to_stata('animals.dta',  None,  True,  None,  None,  None,  None, version=114, convert_strl=None)
