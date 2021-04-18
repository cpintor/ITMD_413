''' GUI using a class '''


from tkinter import Tk, Label, Button
import sys


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title('A Simple GUI')

        self.label = Label(master, text='This is our first GUI')
        self.label.pack()

        self.greet_button = Button(master, text='Greet', command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text='Close', command=master.quit)
        self.close_button.pack()

    def greet(self):
        print('Greeting!')

    def quit(self):
        sys.quit


# Start of program
win = Tk()
my_gui = MyFirstGUI(win)
win.mainloop()