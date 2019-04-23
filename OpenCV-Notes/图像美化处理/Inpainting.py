import cv2
import numpy as np
img = cv2.imread('img1.jpg',1)
cv2.imshow('src',img)
#破坏图像
for i in range(100,200):
    img[i, 100] = (255,255,255)
    img[i, 100+1] = (255,255,255)
    img[i, 100+1] = (255,255,255)
for i in range(50,150):
    img[150, i] = (255,255,255)
    img[150+1, i] = (255,255,255)
    img[150-1, i] = (255,255,255)
cv2.imwrite('damaged.jpg',img)
#修复图像
cv2.imshow('damage', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
paint = np.zeros((height,width,1),np.uint8)
for i in range(100,200):
    paint[i, 100] = 255
    paint[i, 100+1] = 255
    paint[i, 100+1] = 255
for i in range(50,150):
    paint[150, i] = 255
    paint[150+1, i] = 255
    paint[150-1, i] = 255

cv2.imshow('paint',img)
imgdst = cv2.inpaint(img,paint,3,cv2.INPAINT_TELEA)
cv2.imshow('dst',imgdst)
cv2.waitKey(0)
