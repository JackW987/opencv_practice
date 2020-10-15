import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# img = cv.imread('img-1.jpg')
# hist = cv.calcHist([img],[0],None,[256],[0,256])
# hist_numpy,bins = np.histogram(img.ravel(),256,[0,256])
# plt.subplot(121),plt.imshow(img),plt.title('original')
# plt.subplot(122),plt.hist(img.ravel(),256,[0,256]),plt.title('x_y_img')
# plt.show()
# img = cv.imread('white.png')
# cols,rows = img.shape[:2]
# img[0:rows,0:150] = [255,0,0]
# img[0:rows,150:300] = [0,255,0]
# img[0:rows,300:450] = [0,0,255]
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()



# img = cv.imread('img-2.jpg')
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv.calcHist([img],[i],None,[256],[0,256])
#     print(i)
#     print(col)
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()

img = cv.imread('img-2.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:1200, 100:1200] = 255
masked_img = cv.bitwise_and(img,img,mask = mask)
# 计算掩码区域和非掩码区域的直方图
# 检查作为掩码的第三个参数
hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()