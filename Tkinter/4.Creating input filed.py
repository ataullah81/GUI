from tkinter import *


root = Tk()
root.title('First interface')
root.geometry('400x300')

en_box= Entry(root, width=50, bg='green',fg='white',borderwidth=10)
en_box.pack()
en_box.insert(0,"Enter your name: ")


def clickMe():
    #
    hello= 'Hello ' + en_box.get()
    lbl = Label(root,text=hello)
    lbl.pack()

# can change the button size with the help of padx and pady
btn = Button(root,text='Enter you name',font=('Helvetica',20), padx=20,pady=20,fg='blue', bg='green', command=clickMe)
btn.pack()

root.mainloop()