from tkinter import *

mainwin = Tk()
e = Entry(mainwin,width = 50, borderwidth=5)
e.pack()
def myClick():
    myLabel = Label(mainwin, text="Hello " + e.get())
    myLabel.pack()
button = Button(mainwin, text="Enter your name",command=myClick,fg="red",bg="gray")
button.pack()
mainwin.mainloop()
