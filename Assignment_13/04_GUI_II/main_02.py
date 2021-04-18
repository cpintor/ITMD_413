''' Calculates number of fruit cost entered by a user '''
from tkinter import *

window = Tk()
window.title('Fruits Counter')
window.geometry('650x250')

instructions = Label(window, text='Ener the number of fruits and \nclick Computer button to calculate.')
instructions.grid(column=1, row=0)

lime = Label(window, text='Lime $0.10 each:').grid(column=0, row=1)
kiwi = Label(window, text='Kiwi $0.20 each:').grid(column=0, row=2)

lime1 = Entry(window, width=10)
lime1.grid(column=1, row=1)
kiwi1 = Entry(window, width=10)
kiwi1.grid(column=1, row=2)

lime = Label(window, text='Lime Value: $').grid(column=3, row=1)
kiwi = Label(window, text='Kiwi Value $:').grid(column=3, row=2)

lime2 = Label(window, text='0.00')
lime2.grid(column=4, row=1)
kiwi2 = Label(window, text='0.00')
kiwi2.grid(column=4, row=2)
total = Label(window, text='0.00')
total.grid(column=4, row=7)


def calculate():
    int_lime = int(lime1.get())
    limeRes = int_lime * 0.10
    lime2.config(text=limeRes)

    int_kiwi = int(kiwi1.get())
    kiwiRes = int_kiwi * 0.20
    kiwi2.config(text=kiwiRes)

    totalRes = limeRes + kiwiRes
    total.config(text=totalRes)


Button(window, text='Compute', command=calculate).grid(column=1, row=7)
window.mainloop()
