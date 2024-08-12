import tensorflow as tf
tf.contrib.data.make_csv_dataset('dev.csv',  1,  None,  None,  None,  None,  ',',  True,  '',  True,  None,  True,  10000,  None,  1, num_parallel_reads=1, num_parallel_parser_calls=2, sloppy=False, num_rows_for_inference=1)
