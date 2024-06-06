import polars as pl
df = pl.DataFrame({'a': [3, 6, 1, 1, 6]})
df.select(pl.col('a').rank('average'))
