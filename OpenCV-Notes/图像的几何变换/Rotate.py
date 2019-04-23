import cv2
import numpy as np
img = cv2.imread('img.jpg', 1)
cv2.imshow('src', img)
imginfo = img.shape
height = imginfo[0]
width = imginfo[1]
#旋转矩阵
#mat roate 1 center 2 angle 3 scale
matRotate = cv2.getRotationMatrix2D((height*0.5,width*0.5),180,1)
dst = cv2.warpAffine(img,matRotate,(height,width))
cv2.imshow('dst',dst)
cv2.waitKey()
