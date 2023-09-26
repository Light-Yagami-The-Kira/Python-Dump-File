import numpy
arr = numpy.random.randint(1,50,12)
print(arr)
print(arr.shape)
arr = arr.reshape(3,4)
print(arr)
arr = arr.reshape(4,3)
print(arr)
arr = arr.reshape(6,2)
print(arr)
arr = arr.reshape(12,1)
print(arr)
arr = arr.reshape(4,-1) ## -1 ka matlab ki numpy apne aap hi calculate karlo, but haan first number divisible kar sake area ko
print(arr)
# arr = arr.reshape(-1,-1) ## error throw karega
# print(arr)