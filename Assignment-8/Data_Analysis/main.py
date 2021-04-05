"""
This program demonstrates data analysis using numpy.
"""

import numpy as np
import statistics as st
import csv

with open('/Users/crissyp/projects/ITMD-413/ITMD_413/Assignment-8/Data_Analysis/winequality-red.csv', 'r') as f:
    wines = list(csv.reader(f, delimiter=";"))

wines = np.array(wines[1:], dtype=np.float) # skip first row
print(wines)

print("Number of rows =", wines.shape[0]) # how many rows do we have?
print("row and col", wines.shape) # number of rows and columns
print(wines.dtype)
print(wines[2,3]) # print row 2, col 3
print(wines[0:3,3]) # print first 3 items from 4th col
third_wine = wines[3,:] # print entire third wine data
print(third_wine)

print(third_wine[1]) # display row 3 col 1

# select col 12 only
print("\n Wine quality...")
wines_quality = wines[:,11]
print(wines_quality)

print("\nMin quality:", wines[:,11].min())
print("Max quality:", wines[:,11].max())
print("Mean quality:", wines[:,11].mean())
print("\nMedian value:", st.median(wines[:,11])) # using the statistics lib
print("\nSTD value:", wines[:,11].std())

# Determine wine quality greater than 7
high_quality = wines[:,11] > 7
print("\nHigh quality wine...")
print(wines[high_quality,:].shape[0]) # how many of them

average = wines[:,11].mean()
average_quality = wines[:,11] > average
print("Wine > average value...")
print(wines[average_quality,:].shape[0])