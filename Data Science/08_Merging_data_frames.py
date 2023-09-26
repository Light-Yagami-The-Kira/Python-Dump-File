import pandas as pd
df1 = pd.DataFrame([[1,2,434], [344,566,43]], columns=["A", "B", "C"])
df2 = pd.DataFrame([[0,2,45], [344,99669,43]], columns=["X", "Y", "Z"])
df3 = pd.merge(df1,df2, right_on="X", left_on="A")
print(df1)
print(df2)
print(df3)