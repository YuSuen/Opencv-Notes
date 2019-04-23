import cv2
img = cv2.imread('img.jpg', 1)
imginfo = img.shape
dst = img[100:400, 100:600] #裁剪区域
cv2.imshow('image', dst)
cv2.waitKey(0)