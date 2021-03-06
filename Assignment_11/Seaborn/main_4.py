import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')
sns.distplot(df['petal_length'],hist=False)
plt.show()