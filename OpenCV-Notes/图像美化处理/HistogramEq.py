import cv2
import numpy as np
img = cv2.imread('img1.jpg',1)
#灰度直方图均衡
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('src',gray)
dst1 = cv2.equalizeHist(gray)
cv2.imshow('dst1',dst1)
#彩色直方图均衡
cv2.imshow('src',img)
(b,g,r) = cv2.split(img)#通道分解
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
dst2 = cv2.merge((bH,gH,rH))#通道合并
cv2.imshow('dst2',dst2)
#YUV均衡化
imgYUV = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
cv2.imshow('yuv', imgYUV)
channelsYUV = cv2.split(imgYUV)
channelsYUV[0] = cv2.equalizeHist(channelsYUV[0])
channels = cv2.merge(channelsYUV)
dst3 = cv2.cvtColor(channels, cv2.COLOR_YCrCb2BGR)
cv2.imshow('dst3',dst3)
cv2.waitKey(0)