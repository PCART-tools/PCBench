import tensorflow as tf
tf.contrib.data.make_csv_dataset('./dev.csv',  1,  None,  None,  None,  ',',  True,  '',  True,  None,  None,  True,  1,  None,  1,  1,  2,  False,  tf.float32, num_rows_for_inference=1)
