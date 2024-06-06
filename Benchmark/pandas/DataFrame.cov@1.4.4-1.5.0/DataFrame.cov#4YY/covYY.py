import pandas as pd
df = pd.DataFrame([(1, 2), (0, 3), (2, 0), (1, 1)], columns=['dogs', 'cats'])
df.cov(None,  1)
