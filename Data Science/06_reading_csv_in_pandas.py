import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(3))
print(df['Volume'].dtype)
