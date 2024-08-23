from PIL import Image
img = Image.open('./example.jpg')
rotated_img = img.rotate(45, resample=Image.BICUBIC, expand=True)
