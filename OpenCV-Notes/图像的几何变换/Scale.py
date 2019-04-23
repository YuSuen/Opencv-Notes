import cv2

img = cv2.imread('img.jpg', 1)
imginfo = img.shape
print(imginfo) # (1426, 1426, 3)
height = imginfo[0] #高
width = imginfo[1] #宽
mode = imginfo[2] #通道数
#等比缩放
dstheight = int(height * 0.5)
dstwidth = int(width * 0.5)
dst = cv2.resize(img, (dstwidth,dstheight))
cv2.imshow('image', dst)
cv2.waitKey(0)