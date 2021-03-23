"""
This program takes the arguments from the main program into these functions below for calculation.
Name: Cristian Pintor
"""

def prices(list, sum):
    for num in list:
        sum += eval(num)
    print(list)
    taxes = sum * 0.07
    taxed = lambda sum: taxes + sum
    print("Subtotal = $", format(sum, ',.2f'))
    print('Taxes: $', format(taxes, ',.2f'))
    print('Total with taxes is: $', format(taxed(sum), ',.2f'))



