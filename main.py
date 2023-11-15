from PIL import Image as img

me = img.open("image.png")
bg = img.open("no.jpeg")

bg.paste(me, (175,int(120)), me)

bg.save("iamFake.jpeg")