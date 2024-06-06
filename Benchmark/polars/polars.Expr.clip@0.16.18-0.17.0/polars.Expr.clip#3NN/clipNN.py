import polars as pl
pl.col('a').clip(min_val=1, max_val=10)
