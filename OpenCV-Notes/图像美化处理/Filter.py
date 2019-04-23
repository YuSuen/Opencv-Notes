import cv2
import numpy as np
img = cv2.imread('img2.jpg', 1)
cv2.imshow('img', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
#高斯滤波
dst1 = cv2.GaussianBlur(img,(5,5),1.5)
cv2.imshow('dst1', dst1)
#均值滤波
dst2 = np.zeros((height,width,3),np.uint8)
for i in range(3, height-3):
    for j in range(3, width-3):
        sum_b = int(0)
        sum_g = int(0)
        sum_r = int(0)
        for m in range(-3, 3):
            for n in range(-3, 3):
                (b,g,r) = img[i+m, j+n]
                sum_b = sum_b + int(b)
                sum_g = sum_g + int(g)
                sum_r = sum_r + int(r)
        b = np.uint8(sum_b/36)
        g = np.uint8(sum_g/36)
        r = np.uint8(sum_r/36)
        dst2[i,j] = (b,g,r)
cv2.imshow('dst2',dst2)
#中值滤波
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('gray', img)
dst3 = np.zeros((height,width,3), np.uint8)
collect = np.zeros(9, np.uint8)
for i in range(1,height-1):
    for j in range(1, width-1):
        k = 0
        for m in range(-1, 2):
            for n in range(-1, 2):
                gray = img[i+m,j+n]
                collect[k] = gray
                k=k+1
        for k in range(0, 9):
            p1=collect[k]
            for t in range(k+1, 9):
                if p1<collect[t]:
                    mid=collect[t]
                    collect[t]=p1
                    p1 = mid
        dst3[i,j] = collect[4]
cv2.imshow('dst3', dst3)
cv2.waitKey()