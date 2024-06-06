from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False, samplewise_center=False, featurewise_std_normalization=False, samplewise_std_normalization=False)
