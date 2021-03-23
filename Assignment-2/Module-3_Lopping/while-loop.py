# Create a variable to control the loop

keep_going = 'y'

while keep_going == 'y':
    # Get salesperson's sales and commission rate
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))
    # Calculate the commission
    commission = sales * comm_rate

    print("The commission is $", format(commission, '.2f'))

    keep_going = input("Do you want to calculate another commission? (enter y/n): ")
