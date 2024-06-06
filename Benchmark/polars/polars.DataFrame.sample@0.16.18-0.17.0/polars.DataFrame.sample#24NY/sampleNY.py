import polars as pl
df = pl.DataFrame({'foo': [1, 2, 3], 'bar': [6, 7, 8], 'ham': ['a', 'b', 'c']})
df.sample(seed=0, with_replacement=False, shuffle=False, n=2, frac=None)
