import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# img = cv.imread('img-1.jpg',0)
# rows,cols = img.shape
# M = np.float32([[1,0,0],[0,2,0]])
# dst = cv.warpAffine(img,M,(cols,rows))
# cv.imshow('img',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# img = cv.imread('img-1.jpg')
# rows,cols,channel = img.shape
# print('cols:',cols,'pass')
# print('rows:',rows)
# print((cols-1)/2.0)
# print((rows-1)/2.0)
# M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
# dst = cv.warpAffine(img,M,(cols,rows))
# cv.imshow('img',dst)
# cv.waitKey(0)

# img = cv.imread('frame.jpg')
# rows,cols,ch = img.shape
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv.getAffineTransform(pts1,pts2)
# dst = cv.warpAffine(img,M,(cols,rows))
# plt.subplot(1,2,1)
# plt.imshow(img)
# plt.title('Input')
# plt.subplot(1,2,2)
# plt.imshow(dst)
# plt.title('Output')
# plt.show()

img = cv.imread('img-1.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()