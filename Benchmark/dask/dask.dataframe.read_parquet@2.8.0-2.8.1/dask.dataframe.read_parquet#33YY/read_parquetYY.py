import dask.dataframe as dd
ddf = dd.read_parquet('example.parquet',  None, filters=None, categories=None, index=None, storage_options=None, engine='auto')
