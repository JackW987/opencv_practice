import numpy as np
import cv2 as cv
img = cv.imread('wall-2.jpg')
height,width,channel= img.shape[:3]
print(height)
print(width)
print(channel)
res = cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)
cv.imshow('img',res)
cv.waitKey(0)