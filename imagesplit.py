import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.filters import prewitt_h,prewitt_v

img = cv2.imread('Simul1.jpeg')

# Method 1: copy image and set other channels to black
r = img.copy()
r[:,:,0] = r[:,:,1] = 0

g = img.copy()
g[:,:,0] = g[:,:,2] = 0

b = img.copy()
b[:,:,1] = b[:,:,2] = 0

cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Method 2: split channels and merge with black channels
b,g,r = cv2.split(img)
k = np.zeros_like(b)
print("Black array",k)
#plt.plot(k)
#plt.show()
b = cv2.merge([b,k,k])
print("Blue array",b)
#plt.plot(b[:,1])
plt.hist(b.ravel(), bins=10, range=(0.0, 1000.0), fc='k', ec='k')
plt.show()
g = cv2.merge([k,g,k])
plt.hist(img.ravel(), bins=10, range=(0.0, 1000.0), fc='k', ec='k')
plt.show()
r = cv2.merge([k,k,r])

cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save results
cv2.imwrite("mandril3_red.jpg", r)
cv2.imwrite("mandril3_green.jpg", g)
cv2.imwrite("mandril3_blue.jpg", b)
img = imread('Simul1.jpeg',as_gray=True)
#calculating horizontal edges using prewitt kernel
img_h = prewitt_h(img)
#calculating vertical edges using prewitt kernel
img_v = prewitt_v(img)
print("Image H",img_h)
print("Image V", img_v)

#cv2.imwrite(img_h,'test.jpeg')
imshow(img_h,cmap='gray');
plt.show()
imshow(img_v,cmap='gray');
plt.show()

#cv2.imwrite(edges_prewitt_vertical,'test.jpeg')
