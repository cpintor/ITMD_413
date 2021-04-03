"""
This program demonstrates Python seaborn
"""

import matplotlib.pyplot as plt
import seaborn as sns


print("Scatter Plot")
x = ['sun','mon', 'fri', 'sat', 'tue', 'wed', 'thu']
y = [5,6.7,4,6,2,4.9,1.8]

ax = sns.stripplot(x,y)
ax.set(xlabel='Days', ylabel='Amount_spend')

plt.title("My First Graph")
plt.show()