import pandas as pd
import numpy as np
# dataFrame = pd.DataFrame([[234,455],[344,34]])
# print(dataFrame)

# dataFrame2 = pd.DataFrame([1,2])
# print(dataFrame2)

# print(dataFrame.shape, dataFrame2.shape)

arr1 = np.array([[2,34,45,5,4,4,5],[445,5,43,4,53,4,5,],[4,5,4,5,4,4,5],[53,5,54,54,45,4,5]])
df = pd.DataFrame(arr1, columns=['A','B','C','D','E','F','G'])
print(df)
print("===========================================================================")
print(df.iloc[1:3,3:5])
print("===========================================================================")
df["new"] = [1,5,5,9]
print(df)
print("===========================================================================")
df.insert(1, "New 1", [0,0,0,0])
print(df)
print("===========================================================================")
df.drop(columns=["A","B"], inplace=True)
print(df)