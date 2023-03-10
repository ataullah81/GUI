from tkinter import *

mainwin = Tk()
label1 = Label(mainwin, text="My first GUI")
lebel2 = Label(mainwin, text="My name is Russell")
label1.grid(row=0, column=0)
lebel2.grid(row=1, column=0)
mainwin.mainloop()
