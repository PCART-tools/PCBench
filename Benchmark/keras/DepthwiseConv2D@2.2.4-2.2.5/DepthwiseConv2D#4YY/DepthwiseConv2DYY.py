from keras.models import Sequential
from keras.layers import DepthwiseConv2D
model = Sequential()
model.add(DepthwiseConv2D((3, 3), strides=(1, 1)))
