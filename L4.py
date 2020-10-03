import cv2 as cv
img = cv.imread('img-1.jpg')
cv.imshow('img',img)
k = cv.waitKey(0)
if k == ord('s'):
    print('pass')
else:
    print('false')
