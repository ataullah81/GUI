
from tkinter import *




root = Tk()
root.geometry('400x400')

#Dropdown boxes

def show():
    lbl = Label(root, text=clicked.get()).pack()


options = ['Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday',
            'Saturday',
           'Sunday']

clicked =  StringVar()
clicked.set(options[0])


drp_down = OptionMenu(root, clicked, *options )
drp_down.pack()
btn = Button(root, text='Show Selection',command=show).pack()
root.mainloop()