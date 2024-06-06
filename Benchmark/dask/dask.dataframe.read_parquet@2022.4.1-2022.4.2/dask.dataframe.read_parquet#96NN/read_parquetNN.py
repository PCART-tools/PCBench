import dask.dataframe as dd
ddf = dd.read_parquet('/home/zhang/Documents/example.parquet',  None,  None,  None,  None,  None,  'auto',  None, ignore_metadata_file=False, metadata_task_size=None, split_row_groups=None, chunksize=None, aggregate_files=None)
