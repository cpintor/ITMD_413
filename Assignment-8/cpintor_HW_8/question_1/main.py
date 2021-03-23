"""
This program creates an array containing the values 1–15,
reshapes it into a 3-by-5 array, then uses indexing and slicing
techniques to perform each of the following operations

Name: Cristian Pintor
"""

import numpy as np

values = np.arange(1, 16) # creating a 1-15 array using arange()
print(values)

reshaped = values.reshape(3, 5) # reshaping array into 3 by 5
print(reshaped)

# Selecting row 2
print('Second row', reshaped[1,:])

# Selecting column 4
print('Column 4',reshaped[:,3])

#  Select rows 0 and 1.
print('Rows 0 and 1', reshaped[0:2,:])

# Select columns 2–4
print('Columns 2-4', reshaped[:,2:4])

# Select the element that is in row 1 and column 4
print('Element in row 1 and column 4:', reshaped[1,4])

# Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.
print('Elements: ', reshaped[0:2,(0,2,4)])


