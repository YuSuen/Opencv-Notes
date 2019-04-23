import cv2
import numpy as np
img = cv2.imread('img.jpg', 1)
cv2.imshow('src', img)
imginfo = img.shape
height = imginfo[0]
width = imginfo[1]
matshift = np.float32([[1, 0, 100], [0, 1, 200]]) #2*3
dst = cv2.warpAffine(img, matshift, (height, width)) # data mat info
cv2.imshow('dst', dst)

# 图像向左位移100px
# dst = np.zeros(img.shape, np.uint8)
# height = imginfo[0]
# width = imginfo[1]
# for i in range(0, height):
#     for j in range(0, width-100):
#         dst[i, j+100] = img[i,j]
# cv2.imshow('image', dst)
cv2.waitKey(0)