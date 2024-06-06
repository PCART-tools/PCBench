import polars as pl
pl.col('a').clip(1, max_val=10)
