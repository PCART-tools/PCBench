from PIL import Image
img = Image.open('./example.jpg')
bbox = img.getbbox()
