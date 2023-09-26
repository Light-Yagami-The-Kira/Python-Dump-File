import numpy as np
arr1 = np.array([[5,1,7,0], [10,86,12,4]])
print(np.sort(arr1, axis=0, kind='mergesort'))
print(np.sort(arr1, axis=1))