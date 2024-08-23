from PIL import EpsImagePlugin
eps_path = './example.eps'
eps_image = EpsImagePlugin.EpsImageFile(eps_path)
eps_image.load()
