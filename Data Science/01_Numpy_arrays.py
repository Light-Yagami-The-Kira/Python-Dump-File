import numpy 
x = numpy.array([45,45])
print(x)
y = numpy.arange(5,1000)
print(y)
z = numpy.arange(10)
Z = z*3
# for item in Z:
#     print(Z)

arr1 = numpy.array([[1,2,3,5],[3,4,5,"d"],[2,4,False,True]])
print(arr1.shape, arr1.dtype)

arr2 = numpy.zeros((3,10))
print(arr2)

arr3 = numpy.ones((3,10))
print(arr3)

arr4 = numpy.empty((3,4))
print(arr4)

arr5 = numpy.array([4,5])
arr6 = numpy.array([2,3])
print(arr5+arr6)
print(arr5-arr6)
print(arr5*arr6)
print(arr5/arr6)
print(arr5//arr6)
print(arr5**arr6)
print(arr5%arr6)

arr7 = numpy.array([3,4,4,55,5,3,4,45,5,5,5])
arr8 = arr7[::-1]
# print(arr8)
arr8[0] = 6
print(arr7)

arr9 = arr8.copy()
arr9[0] = 5
print(arr9, arr8, arr7)