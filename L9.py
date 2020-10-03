import cv2 as cv
import numpy as np
img1 = cv.imread('black.jpg')
img2 = cv.imread('white.jpg')
img_final = cv.add(img2,img1)
print(img_final[100,100])
cv.imshow('img_final',img_final)
cv.waitKey(0)
cv.destroyAllWindows()
