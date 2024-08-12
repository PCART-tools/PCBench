import dask.dataframe as dd
ddf = dd.read_parquet('example.parquet', columns=None, filters=None, categories=None)
