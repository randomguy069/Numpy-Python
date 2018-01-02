import cv2,numpy

myImage = cv2.imread("smallgray.png",0)

#horizontally stacking the images

myImage2 = numpy.hstack((myImage,myImage)) #since hstack takes only 1 arguements. Tuple is used
print(myImage2)

myImage2 = numpy.vstack((myImage,myImage))
print(myImage2)

#horizontal splitting
lst = numpy.hsplit(myImage2,5) #does split into different numpyarray
print(lst)

lst = numpy.vsplit(myImage2,3)
print(lst)
