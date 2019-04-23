import cv2
import numpy as np
newImageInfo = (500,500,3)
dst = np.zeros(newImageInfo, np.uint8)
# 矩形 第5个参数 负值为填充 /正值为线条宽度
cv2.rectangle(dst,(50,100),(200,300),(255,0,0),-1)
# 圆心 半径
cv2.circle(dst, (250,250),(50),(0,255,255), 2,cv2.LINE_AA)
# 轴长(150, 100) 偏转角度 0 圆弧起始角度 0 圆弧终止角度 180
cv2.ellipse(dst,(256,256),(150,100),0,0,180,(255,255,0), -1, cv2.LINE_AA)
# 任意多边形
points = np.array([[150,50],[140,140],[200,170],[250,250],[150,50]], np.int32)
points = points.reshape(-1, 1, 2)
cv2.polylines(dst, [points], True, (0,255,255))

cv2.imshow('dst',dst)
cv2.waitKey(0)