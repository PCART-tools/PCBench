from PIL import Image
img = Image.open('/home/zhang/example.jpg')
img.thumbnail((100, 100),  3)
