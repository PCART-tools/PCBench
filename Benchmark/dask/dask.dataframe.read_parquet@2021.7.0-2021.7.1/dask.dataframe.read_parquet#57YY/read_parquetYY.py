import dask.dataframe as dd
ddf = dd.read_parquet('./example.parquet',  None,  None,  None,  None,  None,  'auto',  None, split_row_groups=None, read_from_paths=None)
