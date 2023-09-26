import numpy as np
a = np.array([4,5,6])
b = np.array([7,8,9])
c = np.array([1,2,4,9,100,9,45])
print(np.sum(a))
print(np.prod(a))
print(np.diff(c))
d = np.array([2+3j, 4-5j])
print(np.conjugate(d))


arr1 = np.array([1,2])
arr2 = np.array([3,4])
print(np.dot(arr1,arr2))
print(np.cross(arr1,arr2))
arrX = np.array([[3,4,5], [1,1,1]])
print(np.sum(arrX, axis = 1))