"""
This program takes the inputs entered on the main file.
Name: Cristian Pintor
"""

def calculation(another, wholesale):
    mark_up = 2.5 # The markup percentage
    another = 'y' # Variable to control the loop.

    while another == 'y' or another == 'Y':
        # Get the item's wholesale cost.
        wholesale = float(input("Enter the item's wholesale cost: "))
        # Validate the wholesale cost.
        while wholesale < 0:
            print('ERROR: the cost cannot be negative.')
            wholesale = float(input('Enter the correct wholesale cost:'))
        # Calculate the retail price.
        x = lambda wholesale: wholesale * mark_up
        # Display the retail price.
        print('Retail price: $', format(x(wholesale), ',.2f'))
        # Do this again?
        another = input('Do you have another item? (Enter y for yes): ')

def prices(listInput):
    for i in range(10):
        listInput.append(eval(input()))

    print(listInput)