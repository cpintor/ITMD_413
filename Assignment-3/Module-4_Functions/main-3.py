"""
This program shows how to create a function.
"""
import random

# This function sends two numbers and call function show_num()
# to display the sum of two numbers
def main():
    x1 = eval(input('Enter a number: '))
    x2 = eval(input('Enter another number: '))
    #total = show_sum(x1, x2)
    #print('The sum is', total)
    print('The sum is', show_sum(x1, x2))

# This function adds the two numbers and displays the result
def show_sum(num1, num2):
    result = num1 + num2
    return result

# Printing the main function
main()