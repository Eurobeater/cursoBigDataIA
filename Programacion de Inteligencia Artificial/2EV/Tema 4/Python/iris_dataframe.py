import pandas as pd
df = pd.read_csv("iris/iris.data", header = None)
# print(df.head())
# print(df.tail())
# print(df.describe())

y = df.iloc[0:100,4].values
print(y)

import numpy as np
y = np.where(y == 'Iris-setosa', -1, 1)

x = df.iloc[0:100,[0,2]].values
print(x)