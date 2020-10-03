import numpy as np
import cv2 as cv
img = cv.imread('img-1.jpg')

#像素值操作
# px = img[100,100]
# b = img[100,100,0]
# g = img[100,100,1]
# r = img[100,100,2]
# print(px)
# print(b)
# print(g)
# print(r)
# img[100,100] = [255,255,255]
# print(img[100,100])
# print(img.item(100,100,0))
# print(img.item(100,100,1))
# print(img.item(100,100,2))
# img.itemset((100,100,0),255)
# print(img.item(100,100,0))
# print(img.shape)
# print(img.size)
# print(img.dtype)

# roi操作
# bla = img[300:580,500:1000]
# img[0:280,0:500] = bla  
# cv.imshow('img',img) 
# cv.waitKey(0)

# #截取通道
# b,g,r = cv.split(img)
# cv.imshow('imgB',b)
# cv.imshow('imgG',g)
# cv.imshow('imgR',r)
# arr = np.zeros(img.shape[:2],dtype='uint8')
# img_a = cv.merge([b,arr,arr])
# cv.imshow('img_a',img_a)
# cv.waitKey(0)

print(img.shape[:2])