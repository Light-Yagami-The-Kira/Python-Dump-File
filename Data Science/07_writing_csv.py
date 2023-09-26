import pandas as pd
data = pd.read_csv('data.csv')
data = data.head(5)
data.to_csv('export.csv', index=False, mode='a')