import dask.dataframe as dd
ddf = dd.read_parquet('example.parquet',  None,  None,  None,  None,  None,  'auto',  None,  False,  None, split_row_groups=None, chunksize=None, aggregate_files=None)
