from keras.models import Sequential
from keras.layers import Conv2DTranspose
model = Sequential()
model.add(Conv2DTranspose(filters=64, kernel_size=(3, 3)))
