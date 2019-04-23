import cv2
import numpy as np
img = cv2.imread('img.jpg', 1) # 读取图像，第一个参数为图像名称，第二个参数为读取类型，0为gray/1为color
# cv2.imwrite('imagetest.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50]) # JPG图像质量 0~100
# cv2.imwrite('imagetest.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0]) # PNG图像压缩比 0~9
# (b, g, r) = img[100, 100] #像素值读取
# for i in range(1, 100):   #像数值写入
#     img[10 + i, 100] = (255, 0, 0)
#print(b, g, r)

cv2.imshow('image', img) # 展示图像

cv2.waitKey(0) #
