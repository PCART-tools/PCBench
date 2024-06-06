from keras.models import Sequential
from keras.layers import Conv2DTranspose
model = Sequential()
model.add(Conv2DTranspose(64,  (3, 3), strides=(1, 1), padding='valid'))
