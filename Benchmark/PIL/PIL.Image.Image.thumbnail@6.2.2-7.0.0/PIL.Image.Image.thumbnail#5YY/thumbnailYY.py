from PIL import Image
img = Image.open('example.jpg')
img.thumbnail(size=(100, 100), resample=3)
