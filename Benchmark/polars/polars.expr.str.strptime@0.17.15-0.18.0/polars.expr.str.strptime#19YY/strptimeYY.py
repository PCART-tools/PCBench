import polars as pl
df = pl.DataFrame({'date_str': ['2021-01-01', '2021-02-01', '2021-03-01']})
a = pl.col('date_str')
a.str.strptime(cache=True, utc=False, dtype=pl.Date, exact=True, strict=True)
