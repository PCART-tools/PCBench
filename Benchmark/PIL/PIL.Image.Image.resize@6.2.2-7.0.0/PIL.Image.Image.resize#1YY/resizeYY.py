from PIL import Image
image = Image.open('example.jpg')
resized_image_resample = image.resize((100, 100))
