import numpy
# generally images are represented in this format[[123,12,123,12,33],[],[]]

n = numpy.arange(27) #creating a numpy array of 27 numbers
print(n)
print(type(n))

n.reshape(3,9) #converting the single dimensional array to 2 dimensional
print(n)

n.reshape(3,3,3) #converting to three dimensional array
print(n)

m = numpy.asarray([[123,12,123,12,33],[],[]]) #converting to numpy array
print(m)
