import cv2
import numpy as np
img = cv2.imread('img.jpg', 1)
# cv2.imshow('src', img)
imginfo = img.shape
height = imginfo[0]
width = imginfo[1]
deep = imginfo[2]
newimginfo = (height*2, width*2, deep)
dst = np.zeros(newimginfo, np.uint8)
for i in range(0, height):
    for j in range(0, width):
        dst[i, j] = img[i, j]
        dst[height*2-i-1, j] = img[i, j]
for i in range(0, width):
    dst[height, i]=(0,0,255)

cv2.imshow('image', dst)
cv2.waitKey(0)