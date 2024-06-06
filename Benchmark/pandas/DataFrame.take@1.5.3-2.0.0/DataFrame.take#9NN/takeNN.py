import pandas as pd
import numpy as np
df = pd.DataFrame([('falcon', 'bird', 389.0), ('parrot', 'bird', 24.0), ('lion', 'mammal', 80.5), ('monkey', 'mammal', np.nan)], columns=['name', 'class', 'max_speed'], index=[0, 2, 3, 1])
df.take(indices=[0, 3], axis=0, is_copy=None)
