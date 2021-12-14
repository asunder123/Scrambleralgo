# Importing Image and ImageFilter module from PIL package 
from PIL import Image, ImageFilter 
  
# creating a image object 
im1 = Image.open(r"unscrambled.png") 
  
# applying the Kernel filter
im2 = im1.filter(ImageFilter.Kernel((3, 3),
      (-1, -1, -1, -1, 9, -1, -1, -1, -1), 1, 0))
  
im2 = im2.show()
