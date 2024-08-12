import dask.dataframe as dd
ddf = dd.read_parquet('example.parquet',  None,  None,  None, index=None, storage_options=None, engine='auto', gather_statistics=None)
