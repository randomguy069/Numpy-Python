import cv2
myImage = cv2.imread("smallgray.png",0)
#splicing the array that is obtained
print(myImage[0:2])
print(myImage[0:2,2:4])
print(myImage.shape) #returns dimensions of the array

#printing the individual rows of the array
for i in myImage:
    print(i)

#printing individual values of the array
for i in myImage.flat:
    print(i)
