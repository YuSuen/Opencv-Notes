# 1 0-255 2 概率
# 本质：统计每个像素灰度 出现的概率 0-255 p
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('img1.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
count = np.zeros(256, np.float)
for i in range(0, height):
    for j in range(0, width):
        pixel = gray[i,j]
        index = int(pixel)
        count[index] = count[index+1]
for i in range(0,255):
    count[i] = count[i]/(height*width)
x = np.linspace(0, 255, 256)
y = count
plt.bar(x, y, 0.9, alpha=1, color='b')
plt.show()
cv2.waitKey(0)
