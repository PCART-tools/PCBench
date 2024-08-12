import dask.dataframe as dd
ddf = dd.read_parquet('example.parquet',  None, filters=None, categories=None, index=None, storage_options=None, engine='auto', gather_statistics=None, split_row_groups=None, read_from_paths=None)
