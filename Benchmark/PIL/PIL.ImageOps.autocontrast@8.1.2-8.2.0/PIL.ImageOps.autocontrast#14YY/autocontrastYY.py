from PIL import ImageOps, Image
image = Image.open('./example.jpg')
result = ImageOps.autocontrast(image=image, cutoff=0, ignore=None, mask=None)
