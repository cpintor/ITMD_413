import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# if location of file is in local drive
titanic = pd.read_csv('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment_11/Seaborn/titanic.csv')

# number of passengers in each class
sns.countplot(x='Class', data=titanic, palette='Blues')
plt.show()