# How to explore a Pandas series
import pandas as pd
import matplotlib.pyplot as plt

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
print('\n', movies.head())
print('\n', movies.dtypes)  # examine the data type of each Series
print('\n', movies.describe())
print('\n', movies.genre.describe())  # count the non-null values, unique values, and frequency of the most common value
print('\n', movies.genre.value_counts())  # count how many times each value in the Series occurs
print('\n', movies.genre.value_counts(normalize=True))  # display percentages instead of raw counts
print('\n', type(movies.genre.value_counts()))  # 'value_counts' (like many pandas methods) outputs a Series
print('\n', movies.genre.value_counts().head())  # thus, you can add another Series method on the end
print('\n', movies.genre.unique())  # display the unique values in the Series
print('\n', movies.genre.nunique())  # count the number of unique values in the Series

# compute a cross-tabulation of two Series
two_series = pd.crosstab(movies.genre, movies.content_rating)
print('\n', two_series)
print('\n', movies.duration.describe())  # calculate various summary statistics
print('\n', movies.duration.mean()) # many statistics are implemented as Series methods
print('\n', movies.duration.value_counts()) # counts minutes for duration of movie



