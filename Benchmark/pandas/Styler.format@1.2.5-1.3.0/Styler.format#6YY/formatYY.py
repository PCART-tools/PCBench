import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4, 2), columns=['a', 'b'])
df.style.format('{:.2%}',  None,  None)
