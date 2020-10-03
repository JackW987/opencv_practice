import cv2 as cv
img = cv.imread(r"img-1.jpg",0)
cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.imshow('frame',img)
cv.imwrite('gray_1.jpg',img)