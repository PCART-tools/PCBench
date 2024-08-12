from PIL import Image
image = Image.open('example.jpg')
resized_image_resample = image.resize(size=(100, 100))
