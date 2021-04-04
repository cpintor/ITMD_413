import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')
# sns.distplot(df['petal_length'],hist=False)
# sns.distplot(df['petal_length'],kde=False)
# sns.swarmplot(x='species',y='petal_length',data=df)

df = sns.load_dataset("tips")
# sns.violinplot(x='day',y='total_bill',data=df)

# using two sets
sns.regplot(x='total_bill',y='tip',data=df)
sns.lmplot(x='total_bill',y='tip',data=df)
plt.show()


