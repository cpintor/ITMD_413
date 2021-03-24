"""
This program demonstrates data analysis using pandas.
The program uses Avocados.csv
"""

import csv
import pandas as pd

data = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment-9/03_Avocado/avocado.csv')
df = pd.DataFrame(data) # converting csv as data frame
# print(df)

# print(df.head())

print("\nDisplay all rows on columns AveragePrice and Region")
avg_region = df.loc[1:,['AveragePrice','region']]
print(avg_region)

print("\nDisplay price statistics in all regions")
selected_col = df.loc[1:,['AveragePrice']]
print(selected_col.describe())

print("\nDisplay prices statistics in Chicago region only")
chicago_rows = df.loc[df['region'] == 'Chicago']
avg_price = chicago_rows.loc[1:,['AveragePrice']]
print(avg_price.describe())
print(avg_price.describe().stack()[['mean','min','max']])

total_vol = chicago_rows['Total Volume'].sum()
print('\nTotal volume of avocados in Chicago: ', total_vol)