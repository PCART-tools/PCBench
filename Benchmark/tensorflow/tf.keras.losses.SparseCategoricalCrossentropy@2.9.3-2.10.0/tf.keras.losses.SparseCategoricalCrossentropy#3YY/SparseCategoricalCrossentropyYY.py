import tensorflow as tf
scce = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
