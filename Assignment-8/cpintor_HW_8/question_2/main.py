"""
This program takes grades from a CSV file and outputs
different values gathered from the data and also produces a pie chart.
Name: Cristian Pintor
"""


import numpy as np
import statistics as st
import csv
import matplotlib.pyplot as plt

with open('/Users/crissyp/projects/ITMD-413/Assignment-8/cpintor_HW_8/question_2/Student_Grades.csv', 'r') as f:
    students = list(csv.reader(f, delimiter=","))

students = np.array(students[1:], dtype=np.float64) # skip first row
print(students)

# Determine how many students were in the dataset?
print("Number of students =", students.shape[0])

# Display the number of rows and columns of your numpy array.
print("Number of rows and columns", students.shape)

# Display the array data types
print(students.dtype)

print('\nDescriptive Statistics...')
# Min score
print("Min overall score:", students[:,-1].min())

# Max score
print("Max overall score:", students[:,-1].max())

# Mean score
print("Mean score:", students[:,-1].mean())

# Median score
print("Median value:", st.median(students[:,-1]))

# STD
print("STD value:", students[:,-1].std())

# Percentile
twenty_five = np.percentile(students, 25)
seventy_five = np.percentile(students, 75)
print("Percentile (25%, 75%):", twenty_five, seventy_five)

# Number of scores for each grade
print('\nNumber of students achieved in each grade category:')
a = ((89 < students[:,-1]) & (students[:,-1] < 101)).sum()
b = ((79 < students[:,-1]) & (students[:,-1] < 90)).sum()
c = ((69 < students[:,-1]) & (students[:,-1] < 80)).sum()
d = ((59 < students[:,-1]) & (students[:,-1] < 70)).sum()
f = (students[:,-1] < 60).sum()

print(a, 'A')
print(b, 'B')
print(c, 'C')
print(d, 'D')
print(f, 'F')

# Plotting grades in pie chart
grades = [a, b, c, d ,f]
print(grades)

grade_labels = ['A', 'B', 'C', 'D', 'F']

plt.pie(grades, labels=grade_labels)

plt.show()





