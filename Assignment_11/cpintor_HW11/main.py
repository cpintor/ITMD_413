"""
This program demonstrates Python seaborn
Name: Cristian Pintor
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing file
workers = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/cpintor_HW11/workerstips.csv')
flights = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/cpintor_HW11/flightsData.csv')
titanic = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/cpintor_HW11/titanic.csv')

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
wd_4 = sns.relplot(x='total_bill', y='tip', data=workers, hue='smoker')
#
# # labeling
plt.title('Tips Earned vs Total Bill: Lunch vs. Dinner')
plt.xlabel('Total bill')
plt.ylabel('Tips Earned')
plt.show()

# It looks like people tip better during dinner than lunch.

#####################
# e)
#####################
# Finding average per month/year
flight_data = flights.pivot('year', 'month', 'passengers')
fd = sns.lineplot(data=flight_data)

# labeling
plt.title('Average Number of Passengers per Month')
plt.xlabel('Year')
plt.ylabel('Passengers')
plt.show()

# f
data = pd.read_csv('titanic.csv')
df = pd.DataFrame(data)

women = []
men = []
children = []
who = []

w = 0
ma = 0
c = 0

f = df.loc[df['Sex'] == 'female']
m = df.loc[df['Sex'] == 'male']

child = df.loc[df['Age'] < 18]
woman = f.loc[f['Age'] >= 18]
man = m.loc[m['Age'] >= 18]

women = woman['Age'].values.tolist()
men = man['Age'].values.tolist()
children = child['Age'].values.tolist()

for line in women:
    w +=1
    who.append('Women')

for line in men:
    ma +=1
    who.append('Men')

for line in children:
    c +=1
    who.append('Children')

# new df with women, men and children divisions
tWho = pd.DataFrame(who)

# concatenate new df with existing dataset
titanic_data = pd.concat([titanic, tWho], ignore_index=True, axis=1)
titanic_index = titanic_data.rename(columns={0: 'PassengerId', 1: 'Survived', 2: 'Class', 3: 'Name', 4: 'Sex', 5: 'Age', 6: 'SibSp', 7: 'Parch', 8: 'Ticket', 9: 'Fare', 10: 'Cabin', 11: 'Embarked', 12: 'Who'})
print(titanic_index.tail())
titanic_final = titanic_index.dropna(subset=['Who'])
print(titanic_final.tail())

# plot graphs
fx = sns.catplot(x='Class', col='Survived', data=titanic_final, hue='Who', kind='count')
plt.show()
