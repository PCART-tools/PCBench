import pandas as pd
df = pd.DataFrame({'animal': ['falcon', 'parrot', 'falcon', 'parrot'], 'speed': [350, 18, 361, 15]})
df.to_stata('animals.dta', convert_dates=None, write_index=True, byteorder=None, time_stamp=None, data_label=None, variable_labels=None, version=114)
