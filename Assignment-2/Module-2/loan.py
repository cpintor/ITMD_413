'''
This program determines whether a bank customer qualifies for a loan.
Customer must have salary 30k or work  year >= 2, then qualifies for the loan.
'''

min_salary = 3000.0
min_years = 2

salary = eval(input("Enter your annual salary: "))
years_on_job = eval(input("Enter the number of years employed: "))

if salary >= min_salary or years_on_job >= min_years:
    print("You qualify for the loan")
else:
    print("You do not qualify for the loan")