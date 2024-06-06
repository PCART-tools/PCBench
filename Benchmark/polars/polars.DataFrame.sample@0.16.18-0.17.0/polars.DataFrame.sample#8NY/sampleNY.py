import polars as pl
df = pl.DataFrame({'foo': [1, 2, 3], 'bar': [6, 7, 8], 'ham': ['a', 'b', 'c']})
df.sample(with_replacement=False, frac=None, shuffle=False, seed=0)
