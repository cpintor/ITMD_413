'''
This program creates a pairplot from Seaborn to visualize the
California Housing dataset.

Name: Cristian Pintor
'''


import pandas as pd
import seaborn as sns

housing = pd.read_csv('/ITMD_413/Assignment_14/cpintor_HW14/housing.csv')

axes = sns.pairplot(data=housing, vars=housing.columns[0:8])

import matplotlib.pyplot as plt
plt.show()
