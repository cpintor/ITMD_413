'''
This program takes input for  the number of each type of coin a user has in
their possession and then compute and display the total dollar and cents value of these coins
Name : Cristian Pintor
'''

from tkinter import *

window = Tk()
window.title('Fruits Counter')
window.geometry('600x250')
window.configure(background='light yellow')

instructions = Label(window, text='Enter the number of each coin type and hit, Compute:')
instructions.grid(column=1, row=0)

quarters = Label(window, text='Quarters:').grid(column=0, row=1)
dimes = Label(window, text='Dimes:').grid(column=0, row=2)
nickels = Label(window, text='Nickels:').grid(column=0, row=3)
pennies = Label(window, text='Pennies:').grid(column=0, row=4)
h_dollar = Label(window, text='Half dollar:').grid(column=0, row=5)
dollar = Label(window, text='Dollar:').grid(column=0, row=6)

quarters1 = Entry(window, width=10)
quarters1.grid(column=1, row=1)
dimes1 = Entry(window, width=10)
dimes1.grid(column=1, row=2)
nickels1 = Entry(window, width=10)
nickels1.grid(column=1, row=3)
pennies1 = Entry(window, width=10)
pennies1.grid(column=1, row=4)
h_dollar1 = Entry(window, width=10)
h_dollar1.grid(column=1, row=5)
dollar1 = Entry(window, width=10)
dollar1.grid(column=1, row=6)

quarters = Label(window, text='Quarter Value: $').grid(column=2, row=1)
dimes = Label(window, text='Dime Value: $').grid(column=2, row=2)
nickles = Label(window, text='Nickel Value: $').grid(column=2, row=3)
pennies = Label(window, text='Penny Value: $').grid(column=2, row=4)
h_dollar = Label(window, text='Penny Value: $').grid(column=2, row=5)
dollar = Label(window, text='Penny Value: $').grid(column=2, row=6)

quarters2 = Label(window, text='0.00')
quarters2.grid(column=3, row=1)
dimes2 = Label(window, text='0.00')
dimes2.grid(column=3, row=2)
nickels2 = Label(window, text='0.00')
nickels2.grid(column=3, row=3)
pennies2 = Label(window, text='0.00')
pennies2.grid(column=3, row=4)
h_dollar2 = Label(window, text='0.00')
h_dollar2.grid(column=3, row=5)
dollar2 = Label(window, text='0.00')
dollar2.grid(column=3, row=6)

total = Label(window, text='0.00')
total.grid(column=3, row=7)


def calculate():
    int_quarter = int(quarters1.get())
    quarterRes = int_quarter * 0.25
    quarters2.config(text=quarterRes)

    int_dime = int(dimes1.get())
    dimeRes = int_dime * 0.10
    dimes2.config(text=dimeRes)

    int_nickel = int(nickels1.get())
    nickelRes = int_nickel * 0.05
    nickels2.config(text=nickelRes)

    int_penny = int(pennies1.get())
    pennyRes = int_penny * 0.01
    pennies2.config(text=pennyRes)

    int_h_dollar = int(h_dollar1.get())
    h_dollarRes = int_h_dollar * 0.50
    h_dollar2.config(text=h_dollarRes)

    int_dollar = int(dollar1.get())
    dollarRes = int_dollar * 1.00
    dollar2.config(text=dollarRes)

    if quarterRes < 0 or dimeRes < 0 or nickelRes < 0 or pennyRes < 0 or h_dollarRes < 0 or dollarRes <0:
        instructions = Label(window, text='Cannot be negative value')
        instructions.grid(column=1, row=8)
    else:
        totalRes = quarterRes + dimeRes + nickelRes + pennyRes + h_dollarRes + dollarRes
        total.config(text=totalRes)


Button(window, text='Compute', command=calculate).grid(column=1, row=7)
window.mainloop()
