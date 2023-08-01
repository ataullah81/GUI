from tkinter import *


root = Tk()
root.title('First interface')
root.geometry('300x300')

# Creating label
lbl = Label(root, text='This is a test label')
lbl2 = Label(root, text='I am Russell')
# Showing it onto the screen
lbl.grid(row=0,column=0)
lbl2.grid(row=0,column=1)

root.mainloop()