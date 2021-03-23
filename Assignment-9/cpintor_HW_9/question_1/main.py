"""
Write a program on the following two questions. Both Sections A and B should be written in one
program.
Name: Cristian Pintor
"""

import pandas as pd

# Section A
# a. Create a Series from the list [7, 11, 13, 17].
a = pd.Series([7, 11, 13, 17])
print(a)

# b. Create a Series with five elements that are all 100.0.
b = pd.Series([100.0])
print(b.repeat(5))

# c. Create a Series with 20 elements that are all random numbers in the
# range 0 to 100. Use method describe to produce the Series’ basic descriptive
# statistics.
