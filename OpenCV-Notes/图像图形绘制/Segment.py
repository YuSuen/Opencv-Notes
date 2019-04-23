import cv2
import numpy as np
newImageInfo = (500,500,3)
dst = np.zeros(newImageInfo, np.uint8)
#line
#绘制线段 1 dst 2 begin 3 end 4 color
# cv2.line(dst, (100,100),(400,400),(0,0,255))
# 线条宽度 20
# cv2.line(dst, (100,200),(400,200),(0,255,255), 20)
# 防锯齿化
# cv2.line(dst, (100,300),(400,300),(0,255,0), 20, cv2.LINE_AA)
# 三角形绘制
cv2.line(dst,(200,150),(50,250),(25,100,255))
cv2.line(dst,(50,250),(400,380),(25,100,255))
cv2.line(dst,(400,380),(200,150),(25,100,255))
cv2.imshow('dst',dst)
cv2.waitKey()