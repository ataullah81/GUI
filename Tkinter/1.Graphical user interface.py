from tkinter import *


root = Tk()
root.title('First interface')
root.geometry('300x300')

# Creating label
lbl = Label(root, text='This is a test label')
# Showing it onto the screen
lbl.pack()

root.mainloop()