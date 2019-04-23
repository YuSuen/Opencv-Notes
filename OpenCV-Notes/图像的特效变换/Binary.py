import cv2
import numpy as np
def binary_threshold(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1,w*h])
    mean = m.sum()/(w*h)
    print("mean:", mean)
    ret, binary = cv2.threshold(gray, mean, 255, cv2.THRESH_BINARY)
    # cv2.namedWindow("binary2", cv2.WINDOW_NORMAL)
    cv2.imshow("binary2", binary)
    cv2.waitKey(0)

img = cv2.imread("./img1.jpg", 1)
binary_threshold(img)