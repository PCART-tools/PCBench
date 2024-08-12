from PIL import Image
img = Image.open('example.jpg')
rotated_img = img.rotate(angle=45, resample=Image.BICUBIC, expand=True)
