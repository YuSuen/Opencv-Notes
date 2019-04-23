import cv2
import numpy as np
#p = p*1.2+ 40
img = cv2.imread('img2.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
dst = cv2.bilateralFilter(img, 15, 50, 50)
cv2.imshow('dst',dst)
cv2.waitKey(0)