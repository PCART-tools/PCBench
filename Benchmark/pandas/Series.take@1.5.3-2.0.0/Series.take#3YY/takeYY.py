import pandas as pd
import numpy as np
df = pd.Series([('falcon', 'bird', 389.0), ('parrot', 'bird', 24.0), ('lion', 'mammal', 80.5), ('monkey', 'mammal', np.nan)], index=[0, 2, 3, 1])
df.take([0, 3],  0)
