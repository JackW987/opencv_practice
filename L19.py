import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math

# img = cv.imread('img-1.jpg')
# hist = cv.calcHist([img],[0],None,[256],[0,256])
# img_bright = cv.convertScaleAbs(img,alpha=1.5,beta=0)
# hist_bright = cv.calcHist([img_bright],[0],None,[256],[0,256])
# plt.subplot(121),plt.plot(hist,color = 'b')
# plt.subplot(122),plt.plot(hist_bright,color = 'g')
# plt.show()
# cv.imshow("img",img)
# cv.imshow("img_bright",img_bright)
# cv.waitKey(0)
# cv.destroyAllWindows()

#coding:utf-8

# img = cv.imread('img-1.jpg')
# a=1.5
# b=0
# y = np.float(a)*img+b
# y[y>255]=255
# y = np.round(y)
# print(y.dtype)
# img_bright= y.astype(np.uint8)

# cv.imshow("img",img)
# cv.imshow('img_y',y)
# cv.imshow("img_bright",img_bright)
# cv.waitKey(0)
# cv.destroyAllWindows()


# img = cv.imread('img-1.jpg')
# out_min=0
# out_max=255

# in_min = np.min(img)
# in_max = np.max(img)

# a=float(out_max-out_min)/(in_max-in_min)
# b=out_min-a*in_min
# img_norm = img*a+b
# img_norm = img_norm.astype(np.uint8)
# cv.imshow("img",img)
# cv.imshow("img_norm",img_norm)
# cv.waitKey(0)
# cv.destroyAllWindows()

# img = cv.imread('img-1.jpg')
# img_norm = img/255.0  #注意255.0得采用浮点数
# img_gamma = np.power(img_norm,0.4)*255.0
# img_gamma = img_gamma.astype(np.uint8)

# cv.imshow("img",img)
# cv.imshow("img_gamma",img_gamma)
# cv.waitKey(0)
# cv.destroyAllWindows()

# img = cv.imread('img-1.jpg',0)
# img_equalize = cv.equalizeHist(img)
# cv.imshow("img",img)
# cv.imshow("img_equalize",img_equalize)
# cv.waitKey(0)
# cv.destroyAllWindows()

img = cv.imread('1.jpg',0)
clahe = cv.createCLAHE(clipLimit= 40.0,tileGridSize=(8,8))
cl1 = clahe.apply(img)
equ = cv.equalizeHist(img)
hist_cl1 = cv.calcHist([cl1],[0],None,[256],[0,256])
hist_equ = cv.calcHist([equ],[0],None,[256],[0,256])
hist_img = cv.calcHist([img],[0],None,[256],[0,256])
cv.imshow('original',img)
cv.imshow('cl1',cl1)
cv.imshow('equ',equ)
plt.subplot(311),plt.plot(hist_cl1)
plt.subplot(312),plt.plot(hist_equ)
plt.subplot(313),plt.plot(hist_img)
plt.show()
cv.waitKey(0)