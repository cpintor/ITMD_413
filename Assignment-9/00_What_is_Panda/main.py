import pandas as pd

ds = pd.Series([2, 4, 6, 8, 10])

print(ds)

print(ds.describe()) # get statistical data info from ds

# Creating a dataframe
data = [1,2,3,4,5]

df = pd.DataFrame(data)
print(df)

# Two dimensional data
data = [['Anna', 21],['Bob', 22],['Clarke',23]]
df = pd.DataFrame(data, columns=['Name','Age'])
print(df)
print(df.describe())