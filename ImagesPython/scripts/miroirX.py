from PIL import Image


im1=Image.open("image.png")
im2=Image.new("RGB", (400,400))

for y in range(400):
  for x in range(400):
   p1=im1.getpixel((x,y))

   im2.putpixel((399-x,y),p1)


#im1.show()
im2.save("image.png")