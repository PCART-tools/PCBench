import pandas as pd
df = pd.DataFrame({'animal': ['falcon', 'parrot', 'falcon', 'parrot'], 'speed': [350, 18, 361, 15]})
df.to_stata(path='animals.dta', convert_dates=None, write_index=True, byteorder=None, time_stamp=None)
