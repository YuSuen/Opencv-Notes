import cv2
import numpy as np
img = cv2.imread('img.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# newp = gray0-gray1+150
dst = np.zeros((height, width, 1),np.uint8)
for i in range(0, height):
    for j in range(0, width - 1):
        grayp0 = int(gray[i, j])
        grayp1 = int(gray[i, j+1])
        newp = grayp0 - grayp1 + 150
        if newp > 255:
            newp = 255
        if newp < 0:
            newp = 0
        dst[i, j] = newp
cv2.imshow('dst', dst)
cv2.waitKey()