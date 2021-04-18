''' This program demonstrates GUI '''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


window = Tk()
window.title("Welcome to GUI Programming")
window.geometry('400x400')
window.configure(background = "white")

a = Label(window ,text = "First Name").grid(row = 0,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)

b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
b1 = Entry(window).grid(row = 1,column = 1)

c = Label(window ,text = "Email Id").grid(row = 2,column = 0)
c1 = Entry(window).grid(row = 2,column = 1)

d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
d1 = Entry(window).grid(row = 3,column = 1)


def ThankYou():
    messagebox.showinfo("Submited", "Thank You!")

btn = ttk.Button(window, text="Submit", command=ThankYou).grid(row=4,column=0)
window.mainloop()


