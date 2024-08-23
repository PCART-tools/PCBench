from PIL import Image
img = Image.open('./example.jpg')
img.thumbnail((100, 100))
