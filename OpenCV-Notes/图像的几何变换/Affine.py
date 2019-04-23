import cv2
import numpy as np
img = cv2.imread('img.jpg', 1)
cv2.imshow('src', img)
imginfo = img.shape
height = imginfo[0]
width = imginfo[1]
#src 3->dst 3 (左上角 左下角 右上角)
matSrc = np.float32([[0,0],[0,height-1],[width-1,0]])
matDst = np.float32([[50,50],[300,height-200],[width-300,100]])
matAff = cv2.getAffineTransform(matSrc, matDst) # mat 1 src 2 dst
dst = cv2.warpAffine(img, matAff,(width,height))
cv2.imshow('dst', dst)
cv2.waitKey()

