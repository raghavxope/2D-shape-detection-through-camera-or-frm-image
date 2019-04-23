import cv2
path = input('Enter the path for the image from this folder')
img = cv2.imread(path,0)
cv2.imshow('Original', img)
   
#Applying Gaussian Filter
filter = cv2.GaussianBlur(img,(5,5),0)
ret, otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

image, contours, hierarchy = cv2.findContours(otsu,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cont = cv2.drawContours(cont, contours, -1, (0,255,0), 3)
#Displaying the Filtered Image
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.imshow('Contours',cont)
cv2.waitKey(0)