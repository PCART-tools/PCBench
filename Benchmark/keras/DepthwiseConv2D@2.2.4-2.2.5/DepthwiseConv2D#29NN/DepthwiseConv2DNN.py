from keras.models import Sequential
from keras.layers import DepthwiseConv2D
model = Sequential()
model.add(DepthwiseConv2D((3, 3),  (1, 1),  'valid',  1,  None,  None, use_bias=True))
