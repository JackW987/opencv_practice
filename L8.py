import cv2 as cv
import numpy as np

# x = np.uint8([250])
# y = np.uint8([10])
# print(cv.add(x,y))
# print(x+y)

# img1 = cv.imread('wall-1.jpg')
# img2 = cv.imread('wall-2.jpg')
# dst = cv.addWeighted(img1,0.7,img2,0.3,0)
# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# img1 = cv.imread('wall-1.jpg')
# img2 = cv.imread('wall-2.jpg')
# img3 = cv.imread('wall-3.jpg')

# img_final = cv.add(img1,img2,img3)
# cv.imshow('img',img_final)
# cv.waitKey(0)
# cv.destroyAllWindows()
  
# img1 = cv.imread('wall-1.jpg')
# img2 = cv.imread('gra.png')
# img2_gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
# ret,mask = cv.threshold(img2_gray,10,255,cv.THRESH_BINARY)
# cv.imshow('img',img2_gray)
# cv.imshow('img-2',mask)
# img2_bg = cv.bitwise_and(img2,img2,mask = mask)
# cv.imshow('img2_bg',img2)
# cv.waitKey(0)
# cv.destroyAllWindows()

img1 = cv.imread('wall-1.jpg')
img2 = cv.imread('data.png')
# img3 = cv.imread('wall-2.jpg')
rows,cols,channel = img2.shape

roi = img1[0:rows,0:cols]
# roi_2 = img3[0:rows,0:cols]

img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# print(mask_inv.shape)
# cv.imshow('img2gray',img2gray)
# cv.imshow('mask',mask)
# cv.imshow('mask_inv',mask_inv)

img1_bg = cv.bitwise_and(roi,roi,mask=mask_inv)
# img_test_2 = cv.add(img1,img3)
# img_test = cv.bitwise_and(img1,img3)
cv.imshow('img1_bg',img1_bg)
# cv.imshow('img_test',img_test)
# cv.imshow('img_test_2',img_test_2)
img2_fg = cv.bitwise_and(img2,img2,mask=mask)
cv.imshow('mask',mask)
cv.imshow('mask_inv',mask_inv)
cv.imshow('img2_fg',img2_fg)
dst = cv.add(img1_bg,img2_fg)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()