import numpy as np
a = np.array([4,5,6,4,63,50,5,5,4])
print(np.where(a==4))
b = np.array([56,364,71,8,45,4544,4])
print(b)
b.sort()
print(b)
print(np.searchsorted(b,57))

