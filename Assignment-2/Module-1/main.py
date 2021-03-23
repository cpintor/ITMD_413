# This program demonstrates Python simple I/O
# Name: Cristian

print("Welcome to Python Programming!") # use single or double quotes to print
print("I'm here to assist.")

num1 = 88.581

# Display number in a field of 7 spaces with 2 decimals points
print(format(num1, '7.2f'))

amount_due = 5000.0
monthly_payment = amount_due / 12
print("The monthly payment is", format(monthly_payment, '.2f'))

name = input("What is your name?")
age = int(input("What is your age?"))
income = float(input("What is your income?"))

print("Here is the data you have entered: ")
print("Name:", name)
print("Age:", age)
print("Income", income)

income = eval(input("What is your income?")) # to read number
print("The income is: %.2f" % income)


