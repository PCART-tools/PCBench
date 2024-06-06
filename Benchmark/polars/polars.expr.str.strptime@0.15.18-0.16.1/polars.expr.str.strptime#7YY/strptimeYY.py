import polars as pl
df = pl.DataFrame({'date_str': ['2021-01-01', '2021-02-01', '2021-03-01']})
a = pl.col('date_str')
df = df.with_column(a.str.strptime(pl.Date,  '%Y-%m-%d', strict=True))
