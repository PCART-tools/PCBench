import tensorflow as tf
d = tf.data.TFRecordDataset(['valid.tfrecord'], compression_type=None)
