import numpy as np

arr = np.arange(10)
# arr = np.array([
#     [2, 4],
#     [6, 8],
#     [9,10]
# ])
print(arr)
for item in range(arr.size):
    print(arr[item])
print(arr[-1])

print(arr[1:5:2])