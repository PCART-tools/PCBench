import dask.dataframe as dd
ddf = dd.read_parquet(path='./example.parquet', columns=None, filters=None, categories=None, index=None, storage_options=None, engine='auto', gather_statistics=None, ignore_metadata_file=False, metadata_task_size=None, split_row_groups=None, chunksize=None)
