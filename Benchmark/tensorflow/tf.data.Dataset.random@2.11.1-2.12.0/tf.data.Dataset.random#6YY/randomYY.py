import tensorflow as tf
ds1 = tf.data.Dataset.random(seed=4, name=None).take(10)
