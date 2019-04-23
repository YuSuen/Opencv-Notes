import cv2
import numpy as np
# 方法1读取时转换为灰度图
# img0 = cv2.imread('img.jpg', 0)
# img1 = cv2.imread('img.jpg', 1)
# print(img0.shape)
# print(img1.shape)
# cv2.imshow('img0',img0)
# cv2.imshow('img1',img1)

img = cv2.imread('img.jpg', 1)
# 方法2利用cvtCOLOR转换
# dst = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('img',dst)

imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

# 方法3RGB R=G=B=Gray (R+G+B)/3
# dst = np.zeros((height, width, 3), np.uint8)
# for i in range(0, height):
#     for j in range(0, width):
#         (b,g,r)=img[i,j]
#         gray = (int(b)+int(g)+int(r))/3
#         dst[i,j] = np.uint8(gray)
# cv2.imshow('dst',dst)

# 方法4gray = r*0.299+g*0.587+b*0.114
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (b,g,r)=img[i,j]
        b = int(b)
        g = int(g)
        r = int(r)
        # gray = r * 0.299 + g * 0.587 + b * 0.114
        # gray = (r * 1 + g * 2 + b * 1)/4
        gray = (r + (g << 1) + b) >>2
        dst[i,j] = np.uint8(gray)
cv2.imshow('dst',dst)
cv2.waitKey()