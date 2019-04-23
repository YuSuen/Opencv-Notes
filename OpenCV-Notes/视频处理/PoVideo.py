import cv2
img = cv2.imread('./image/image1.jpg')
imgInfo = img.shape
size = (imgInfo[1], imgInfo[0])
print(size)
path = './image/'
videoWrite = cv2.VideoWriter('2.mp4', -1, 5, size)
#图片合成视频
for i in range(1, 11):
    fileName =path+'image' + str(i) + '.jpg'
    img = cv2.imread(fileName)
    videoWrite.write(img)#写入
print('end!')