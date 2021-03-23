# Doing calculations using format() and F-String

# # Doing calculations using F-String
# calculation = f'4 times 11 is equal to {4 * 11}'
# print(calculation)


# # Looping thru a range of values and printing them thru each loop
# for n in range(1, 11):
#     sentence = f'The value is {n:02}'  # adding zero padded by 2
#     print(sentence)


# # Floating point values
# pi = 3.14159265
#
# sentence = f'Pi is equal to {pi:.4f}'   # Printing out up to 4 digits
# print(sentence)


# Formatting and printing dates
from datetime import datetime

birthday = datetime(1900, 1, 1)

sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'   # Formatting year
print(sentence)