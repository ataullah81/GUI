from tkinter import *

mainwin = Tk()
e = Entry(mainwin,width=50)
e.pack()


def myClick():
    myLabel = Label(mainwin, text="I click a button", fg="blue")
    myLabel.pack()


button = Button(mainwin, text="Ok", command=myClick, fg="red", bg="gray")
button.pack()
mainwin.mainloop()
