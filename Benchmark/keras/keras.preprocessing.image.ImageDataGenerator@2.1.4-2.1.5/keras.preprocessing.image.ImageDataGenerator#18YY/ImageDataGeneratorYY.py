from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False,  False,  False, samplewise_std_normalization=False, zca_whitening=False)
