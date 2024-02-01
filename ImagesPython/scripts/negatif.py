from PIL import Image
import PIL.ImageOps    
 
image = Image.open("image.png")
 
inverted_image = PIL.ImageOps.invert(image)
 
inverted_image.save('image.png')