import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('thre.jpg')
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thre1 = cv.threshold(img_gray,127,255,cv.THRESH_BINARY)
adaptive_thre1 = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,2)
adaptive_thre2 = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,7,2)

titles = ["img","thre1","adaptive_thre1","adaptive_thre2"]
imgs = [img,thre1,adaptive_thre1,adaptive_thre2]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()