import dask.bag as db
b = db.from_sequence(['apple', 'banana', 'cherry', 'date', 'elderberry'], npartitions=2)
b.to_textfiles('./txts/*.txt',  None,  'infer',  'utf-8',  True, storage_options=None)
