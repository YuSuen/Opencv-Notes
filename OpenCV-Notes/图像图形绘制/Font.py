import cv2
import numpy as np
img1 = cv2.imread('img1.jpg', 1)
img0 = cv2.imread('img.jpg',1)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.rectangle(img, (200,100),(400,200),(0,255,0), 3)
# cv2.putText(img, 'images',(100,200),font,1,(200,100,255),2,cv2.LINE_AA)
# print(img.shape)
# height = int(img.shape[0]*0.2)
# width = int(img.shape[1]*0.2)
# imgResize = cv2.resize(img, (height,width))
# print(imgResize.shape)
height = int(img1.shape[0])
width = int(img1.shape[1])
for i in range(0,height):
    for j in range(0,width):
        img0[i+100,j+200] = img1[i,j]
cv2.imshow('src',img0)
cv2.waitKey(0)