from PIL import Image, ImageOps
image = Image.open('example.jpg')
result_image = ImageOps.autocontrast(image, cutoff=0)
