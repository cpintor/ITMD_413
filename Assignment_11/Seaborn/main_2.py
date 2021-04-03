import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# if location of file is in local drive
titanic = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/Seaborn/titanic.csv')

# Load titanic dataset
# titanic = sns.load_dataset('titanic')

# Plotting how many people survived
# using bar plot to illustrate the avg. number of survivors
# of male and females
sns.barplot(x='Sex', y='Survived', hue='Class', data=titanic)
plt.show()
