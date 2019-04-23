#gray 0~255 255-当前像素值
import cv2
import numpy as np
img = cv2.imread('img.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# gray
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# dst = np.zeros((height, width, 1), np.uint8)
# for i in range(0, height):
#     for j in range(0, width):
#         graypix = gray[i,j]
#         dst[i,j] = 255-graypix
# cv2.imshow('dst',dst)

#color 255-R=newR
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (b,g,r) = img[i,j]
        dst[i,j] = [255-b,255-g,255-r]
cv2.imshow('dst',dst)
cv2.waitKey()