import numpy as np
arr = np.zeros(5)
print(arr)
arr1 = np.zeros((3,5))
print(arr1)

arr2 = np.ones(4)
print(arr2)
arr2 = np.ones((2,4), dtype=int)
print(arr2)

arr = np.eye(3)
print("eye\n", arr)
arr = np.eye(3,4)
print(arr)
arr = np.eye(3,k=1)
print(arr)
print("==============================")
arr = np.diag([1,2,3,4,5,6], k=0)
print(arr)
arr = np.diag([1,2,3,4,5,6], k=1)
print(arr)
arr = np.diag([1,2,3,4,5,6], k=2)
print(arr)
print("==============================")

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