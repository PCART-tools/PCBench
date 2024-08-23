import tensorflow as tf
tf.contrib.data.make_csv_dataset('./dev.csv',  1,  None,  None,  None,  None,  ',',  True,  '',  True,  None, shuffle=True, shuffle_buffer_size=10000, shuffle_seed=None, prefetch_buffer_size=1, num_parallel_reads=1, num_parallel_parser_calls=2, sloppy=False, num_rows_for_inference=1)
