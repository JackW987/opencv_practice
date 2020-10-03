import cv2
img = cv2.imread('img-1.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_threshold = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
print(ret)
cv2.imshow('original',img)
cv2.imshow("img",img_gray)
cv2.imshow("thre",img_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
