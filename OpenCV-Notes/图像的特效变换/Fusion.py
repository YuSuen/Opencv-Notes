#dst = src1*a +src2*(1-a)
import cv2
import numpy as np
img0 = cv2.imread('img.jpg', 1)
img1 = cv2.imread('img1.jpg', 1)
# img0 1426*1426
# img1 300*533
img1= cv2.resize(img1, (1426, 1426))
# print(img0.shape)
# print(img1.shape)
imgInfo = img0.shape
height = imgInfo[0]
width = imgInfo[1]

roiH = int(height)
roiW = int(width)
img0ROI = img0[0:roiH,0:roiW]
img1ROI = img1[0:roiH,0:roiW]

dst=np.zeros((roiH,roiW,3),np.uint8)
dst = cv2.addWeighted(img0ROI,0.5,img1ROI,0.5,0)
cv2.imshow('dst',dst)
cv2.waitKey()

