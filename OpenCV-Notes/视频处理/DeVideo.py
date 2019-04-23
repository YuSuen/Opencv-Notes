import cv2
import os
cap = cv2.VideoCapture('1.mp4')
isOpened = cap.isOpened()#判断是否打开
print(isOpened)
fps = cap.get(cv2.CAP_PROP_FPS)#帧率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps, width, height)
path = './image/'
if (os.path.exists(path))==True:
    os.makedirs(path)
i = 0
while(isOpened):
    if i == 10:
        break
    else:
        i = i + 1
    (flag, fram) = cap.read()#读取视频每一帧图像
    fileName = path+'image' + str(i) + '.jpg'
    print(fileName)
    if flag == True:
        cv2.imwrite(fileName, fram,[cv2.IMWRITE_JPEG_QUALITY,100])
print("end!")