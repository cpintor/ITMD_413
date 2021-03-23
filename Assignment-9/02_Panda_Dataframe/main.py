import numpy as np
import pandas as pd

# 1. load hard-coded data into a dataframe
df = pd.DataFrame([
    ['Jan', 58, 42, 74, 22, 2.95],
    ['Feb', 61, 45, 78, 26, 3.02],
    ['Mar', 65, 48, 84, 25, 2.34],
    ['Apr', 67, 50, 92, 28, 1.02],
    ['May', 71, 53, 98, 35, 0.48],
    ['Jun', 75, 56, 107, 41, 0.11],
    ['Jul', 77, 58, 105, 44, 0.0],
    ['Aug', 77, 59, 102, 43, 0.03],
    ['Sep', 77, 57, 103, 40, 0.17],
    ['Oct', 73, 54, 96, 34, 0.81],
    ['Nov', 64, 48, 84, 30, 1.7],
    ['Dec', 58, 42, 73, 21, 2.56]],
    index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    columns=['month', 'avg_high', 'avg_low', 'record_high', 'record_low', 'avg_precipitation'])

print(df)

# 2. Read text file into a dataframe
filename = 'Fremont_weather.txt'
df = pd.read_csv(filename)
print(df)

# 3. print first 5 or 3 rows of df
print(df.head())
print(df.tail(3))

# 4. get data types index, columns, values
print(df.dtypes)
print(df.index)
print(df.columns)
print(df.values)

# 5 statistical summary of each column
print(df.describe())

# 6 sort records by any column
print(df.sort_values('record_high', ascending=False))

# 7 slicing records
print(df.avg_low) # index with single column

print(df['avg_low'])

print(df['avg_low'])

print(df[2:4]) # index with single column, rows 2 to 3

print(df[['avg_low','avg_high']])

print(df.loc[:,['avg_low','avg_high']]) # multiple columns

print(df.loc[9,['avg_precipitation']])

print(df.iloc[3:5,[0,3]]) # index location can receive range or list of indices

# 8. Filtering
print(df[df.avg_precipitation > 1.0]) # filter on column values
print(df[df['month'].isin(['Jun','Jul','Aug'])])

# 9. Assignment -- very similar to slicing
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
# comment everything except for section 2
df.rename(columns={'avg_precipitation':'avg_rain'}, inplace=True) # rename 1 column
print(df.head())

df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain']
print(df.head())

# 11. iterate a df
for index, row in df.iterrows():
    print(index, row['month'], row['avg_high'])

# 12. write to csv file
df.to_csv('foo.csv')