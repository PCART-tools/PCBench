import polars as pl
pl.col('num').is_between(start=2, end=4)
