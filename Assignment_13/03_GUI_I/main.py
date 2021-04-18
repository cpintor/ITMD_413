''' This program demonstrates GUI interface '''

import tkinter as tk

window = tk.Tk()
window.title('Python GUI')
tk.Label(window, text='A Label').grid(column=0, row=0)


def click_me():
    action.configure(text='I have been clicked!')


action = tk.Button(window, text='Click me', command=click_me)
action.grid(column=1, row=0)

# start GUI
window.mainloop()