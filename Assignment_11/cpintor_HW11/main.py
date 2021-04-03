"""
This program demonstrates Python seaborn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing file
workers = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/cpintor_HW11/workerstips.csv')
flights = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/cpintor_HW11/flightsData.csv')

# a) Using dataset workerstips.csv, create a scatterplot with total_bill
# as the x-axis and the tips as the y-axis.
# sns.scatterplot(x='total_bill', y='tip', data=workers)
# plt.show()

# b)
# sns.scatterplot(data=workers, x='total_bill', y='tip', hue='smoker')
# plt.show()

# c)
# sns.barplot(data=workers, x='day', y='tip')
# plt.show()

# d)
sns.scatterplot(data=workers, x='total_bill', y='tip', hue='time')
plt.show()
# It looks like people tip better during dinner than lunch.

# e)
sns.lineplot(data=flights, x='year', y='passengers')
plt.show()