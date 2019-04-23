import cv2
import numpy as np
img = cv2.imread('img.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# b = b*1.5
# g = g*1.3
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0,height):
    for j in range(0, width):
        (b,g,r) = img[i,j]
        b = b*1.5
        g = g*1.3
        if b > 255:
            b = 255
        if g > 255:
            g = 255
        dst[i, j] = (b, g, r)
cv2.imshow('dst', dst)
cv2.waitKey(0)
