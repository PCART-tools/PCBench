from keras.models import Sequential
from keras.layers import Conv2DTranspose
model = Sequential()
model.add(Conv2DTranspose(64,  (3, 3), strides=(1, 1), padding='valid', output_padding=None, data_format=None, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None))
