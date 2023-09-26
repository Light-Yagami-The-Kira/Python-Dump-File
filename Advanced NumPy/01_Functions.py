import numpy as np
arr = np.zeros(5)
print(arr)
arr1 = np.zeros((3,5))
print(arr1)

arr2 = np.ones(4)
print(arr2)
arr2 = np.ones((2,4))
print(arr2)

arr = np.eye(3)
print(arr)
arr = np.eye(3,4)
print(arr)

arr = np.diag([69,1,2,3,4,5,6])
print(arr)

print(f"Diagonals of the above array are {np.diag(arr)}")

arr = np.random.randint(1,10,10)
print(arr)

arr = np.random.rand(10)
print(arr)

arr = np.random.rand(3,10)
print(arr)

arr = np.random.randn()
print(np.max(arr))

print(np.ndim(arr))