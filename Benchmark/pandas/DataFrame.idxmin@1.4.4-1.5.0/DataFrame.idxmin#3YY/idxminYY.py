import pandas as pd
df = pd.DataFrame({'consumption': [10.51, 103.11, 55.48], 'co2_emissions': [37.2, 19.66, 1712]}, index=['Pork', 'Wheat Products', 'Beef'])
df.idxmin(axis=0)
