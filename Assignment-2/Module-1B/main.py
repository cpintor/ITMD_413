'''
This program demonstrates how to detect
errors on input data entered by user
'''

try:
    n1 = int(input("Enter integer number: "))
    n2 = int(input("Enter second integer number: "))
    sum = n1 + n2
    print("The sum is: ", sum)

except:
    print("Error! Please check your data entry.")





