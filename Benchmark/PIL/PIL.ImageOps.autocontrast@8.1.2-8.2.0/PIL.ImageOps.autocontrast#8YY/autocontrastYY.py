from PIL import ImageOps, Image
image = Image.open('./example.jpg')
result = ImageOps.autocontrast(image, cutoff=0, ignore=None)
