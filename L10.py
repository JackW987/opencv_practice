import cv2 as cv
import numpy as np
img1 = cv.imread('wall-1.jpg')
img2 = cv.imread('data.png')
rows,cols,channels= img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret1,mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
cv.imshow('mask',mask)

mask_not = cv.bitwise_not(mask)
cv.imshow('mask_not',mask_not)

bg_and = cv.bitwise_and(roi,roi,mask = mask_not)
bg_ori = cv.bitwise_and(img2,img2,mask = mask)
cv.imshow('bg_ori',bg_ori)
cv.imshow('bg_and',bg_and)

bg_final = cv.add(bg_and,bg_ori)
cv.imshow('bg_final',bg_final)
img1[0:rows,0:cols] = bg_final
cv.imshow('final',img1)
cv.waitKey(0)

