import cv2
import numpy as np
#p = p + 40
img = cv2.imread('img1.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
dst = np.zeros((height,width,3), np.uint8)
for i in range(0,height):
    for j in range(0, width):
        (b,g,r) = img[i,j]
        # nb = int(b*1.3)+10
        # ng = int(g*1.2)+15
        nb = int(b)+40
        ng = int(g)+40
        nr = int(r)+40
        if nb > 255:
            nb = 255
        if ng > 255:
            ng = 255
        if nr > 255:
            nr = 255
        dst[i,j] = (nb,ng,nr)
cv2.imshow('dst', dst)
cv2.waitKey(0)