import numpy as np
import pandas as pd
import random

dict1 = {
    'name' : np.array(["harry", "rohan", "skillf", "shubh"]),
    'marks' : np.array([23, 56, 57, 90]),
    'name' : np.array(["rampur", "bhopal", "kolkata", "delhi"]),
}

df = pd.DataFrame(dict1)
print(df)

df.to_csv("example.csv", index=False)
print(df.head(2))
print(df.tail(2))
print(df.describe())

a = pd.read_csv("train.csv")
print(a)
print(a.describe())

a["speed"][0] = random.randint(1,100)

print(a)

a.to_csv("train.csv")
