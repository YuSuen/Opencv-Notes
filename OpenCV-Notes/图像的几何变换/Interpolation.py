#最近邻域插值
#src 10*20 dst 5*10
#dst<-src
#(1,2)<-(2,4)
#newx = x*(src_row/dst_row) newx = 1*(10/5) = 2
#newy = y*(src_column/det_column) newy = 2*(20/10) = 4

import cv2
import numpy as np
img = cv2.imread('img.jpg', 1)
imginfo = img.shape
height = imginfo[0]
width = imginfo[1]
dstheight = int(height * 0.5)
dstwidth = int(width * 0.5)
dstimage = np.zeros((dstheight, dstwidth, 3), np.uint8) #0~255
for i in range(0, dstheight):
    for j in range(0, dstwidth):
        newi = int(i * (height * 1.0 / dstheight))
        newj = int(j * (width * 1.0 / dstwidth))
        dstimage[i, j] = img[newi, newj]
cv2.imshow('image', dstimage)
cv2.waitKey(0)

#双线性插值
#A1 = 20% 上+80%下 A2
#B1 = 30% 左+70%右 B2
#1 最终点 = A1 30% + A2 70%
#1 最终点 = B1 20% + B2 80%


