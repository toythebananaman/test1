from PIL import Image, ImageColor
import numpy as np

# Open the image
img = Image.open("image.png")

# Convert the image to HSV
hsv_img = img.convert('HSV')

# Manipulate the HSV values
hsv = np.array(hsv_img)
# For example, to shift the hue
hsv[..., 0] = (hsv[..., 0] + 20) % 256

# Create a new image with the manipulated HSV values
new_img = Image.fromarray(hsv, 'HSV')

# Convert the new image back to RGB
final_img = new_img.convert('RGB')

# Show or save the final image
final_img.show()
final_img.save("edited_image.jpg")
