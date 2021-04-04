"""
This program demonstrates Python seaborn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing file
workers = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/cpintor_HW11/workerstips.csv')
flights = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/cpintor_HW11/flightsData.csv')

#####################
# a)
#####################
# Getting data
wd = sns.scatterplot(x='total_bill', y='tip', data=workers)

# labeling
plt.title('Tips Earned vs Total Bill')
plt.xlabel('Total bill')
plt.ylabel('Tips Earned')

plt.show()

#####################
# b)
#####################
# Getting data
wd_2 = sns.scatterplot(
    data=workers, x='total_bill', y='tip', hue='smoker', style="smoker", size='size',
    sizes=(10,300)
)

# labeling
plt.title('Tips Earned vs Total Bill: Smokers vs. Non-smokers')
plt.xlabel('Total bill')
plt.ylabel('Tips Earned')

plt.show()

#####################
# c)
#####################
wd_3 = sns.barplot(data=workers, x='day', y='tip')

# labeling
plt.title('Tips Earned vs Total Bill: Average Tip Per Day')
plt.xlabel('Day of The Week')
plt.ylabel('Average Tip')

plt.show()

#####################
# d)
#####################
# wd_4 = sns.boxplot(data=workers, x='total_bill', y='tip', hue='time')
#
# # labeling
# plt.title('Tips Earned vs Total Bill: Lunch vs. Dinner')
# plt.xlabel('Total bill')
# plt.ylabel('Tips Earned')
#
# plt.show()
# # It looks like people tip better during dinner than lunch.

#####################
# e)
#####################
fd = sns.lineplot(data=flights, x='year', y='passengers')
# Finding average per month/year


# labeling
plt.title('Average Number of Passengers per Month')
plt.xlabel('Year')
plt.ylabel('Passengers')

plt.show()