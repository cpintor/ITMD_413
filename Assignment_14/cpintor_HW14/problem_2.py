'''
This program reimplements the simple linear regression case study using the
average yearly temperature data.

Name: Cristian Pintor
'''


import pandas as pd

nyc = pd.read_csv('/ITMD_413/Assignment_14/cpintor_HW14/ave_yearly_temp_nyc_1895-2017.csv')

nyc.columns = ['Date', 'Temperature', 'Anomaly']

nyc.Date = nyc.Date.floordiv(100)

# nyc.head(3)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    nyc.Date.values.reshape(-1, 1),
    nyc.Temperature.values,
    random_state=11
)

print(X_train.shape)
print(X_test.shape)

# Training the Model
from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()

linear_regression.fit(X=X_train, y=y_train)
LinearRegression(copy_X=True,
                 fit_intercept=True,
                 n_jobs=None,
                 normalize=False)

print(linear_regression.coef_)
print(linear_regression.intercept_)

predicted = linear_regression.predict(X_test)

expected = y_test

for p, e, in zip(predicted[::5], expected[::5]):
    print(f'predicted: {p:2f}, expected: {e:2f}')

predict = (lambda x: linear_regression.coef_ *
           x + linear_regression.intercept_)

print(predict(2009))
print(predict(1890))

# Visualizing the Dataset with the Regression Line
import seaborn as sns
axes = sns.scatterplot(data=nyc, x='Date',
                       y='Temperature',
                       hue='Temperature',
                       palette='winter',
                       legend=False)

print(axes.set_ylim(10, 70))

import numpy as np
x = np.array([min(nyc.Date.values),
              max(nyc.Date.values)])

y = predict(x)

import matplotlib.pyplot as plt
line = plt.plot(x,y)
plt.show()
