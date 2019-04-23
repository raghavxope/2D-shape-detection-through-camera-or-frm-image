import cv2
path = input('Enter the path for the image from this folder')
img = cv2.imread(path,1)
cv2.imshow('Original', img)
cv2.waitKey(0)
   
#Applying Gaussian Filter
filter = cv2.GaussianBlur(img,(5,5),0)

#Displaying the Filtered Image
cv2.imshow('Filtered', filter)
cv2.waitKey(0)