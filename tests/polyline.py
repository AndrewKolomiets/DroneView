import cv2
import numpy as np
from matplotlib import pyplot as plt

# path
#path = r'gfg.jpeg'
 
# Reading an image in default 
# mode
#image = cv2.imread(path)
image = np.zeros((1000,1000,3), dtype='uint8')
# Window name in which image is 
# displayed
window_name = 'Image'
 
# Polygon corner points coordinates
pts = np.array([[25, 70], [25, 145],
                [75, 190], [150, 190],
                [200, 145], [200, 70], 
                [150, 25], [75, 25]],
               np.int32)
 
pts = pts.reshape((-1, 1, 2))
 
isClosed = True
 
# Green color in BGR
color = (0, 255, 0)
 
# Line thickness of 8 px
thickness = 8
 
# Using cv2.polylines() method
# Draw a Green polygon with 
# thickness of 1 px
cv2.polylines(image, [pts], 
                      isClosed, color, 
                      thickness)
 
plt.imshow(image)
plt.show()