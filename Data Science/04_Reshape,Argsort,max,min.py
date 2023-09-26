import numpy as np
arr1 = np.arange(10)
print(arr1)
print(arr1.reshape(1,10))
print(arr1.reshape(10,1))
print(arr1.reshape(5,2))
print(arr1.reshape(2,5))

arr2 = np.array([1,898,3,56,0,566,45])
print(arr2.argsort())
print((arr2.argsort())[::-1])

print(arr2.argmax())
print(arr2.argmin())

arr3 = np.array([[4,2],[5,1]])
print(arr3)
print(arr3.argsort(axis = 1))
print(arr3.argsort(axis = 0))