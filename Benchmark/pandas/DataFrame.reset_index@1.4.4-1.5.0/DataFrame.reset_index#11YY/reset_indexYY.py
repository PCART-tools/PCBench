import pandas as pd
import numpy as np
df = pd.DataFrame([('bird', 389.0), ('bird', 24.0), ('mammal', 80.5), ('mammal', np.nan)], index=['falcon', 'parrot', 'lion', 'monkey'], columns=('class', 'max_speed'))
df.reset_index(None,  False,  False,  0)
