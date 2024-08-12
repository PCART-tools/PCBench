import dask.dataframe as dd
ddf = dd.read_parquet(path='example.parquet', columns=None, filters=None, categories=None, index=None, storage_options=None)
