import polars as pl
pl.col('foo').reshape(dims=(3, 3))
