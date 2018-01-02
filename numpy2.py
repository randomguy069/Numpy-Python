import cv2
myImage = cv2.imread("smallgray.png",1) #reading the image file
print(myImage)
print(type(myImage))

#converting numpy array to image
cv2.imwrite("newsmallgray.png",myImage)
print(cv2.imwrite("newsmallgray.png",myImage)) #if this returns true means it was a success creating a new image
