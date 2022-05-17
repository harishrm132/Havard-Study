from PIL import Image, ImageFilter

before = Image.open("nadal.jfif")
after = before.filter(ImageFilter.BoxBlur(5))
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.bmp")