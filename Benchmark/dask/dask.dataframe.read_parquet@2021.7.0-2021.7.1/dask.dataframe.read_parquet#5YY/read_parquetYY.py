import dask.dataframe as dd
ddf = dd.read_parquet(path='./example.parquet', columns=None)
