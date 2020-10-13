import cv2 as cv
import numpy as np
# e1 = cv.getTickCount()
# print('test code')
# e2 = cv.getTickCount()
# time = (e2 - e1) / cv.getTickFrequency()
# print(time)

img = cv.imread('wall-1.jpg')
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,1)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print(t)

