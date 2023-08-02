from tkinter import *


root = Tk()
root.title('First interface')
root.geometry('300x300')

def clickMe():
    # After clicking button create a new window and put label on it
    win = Tk()
    win.title('Label')
    win.geometry('200x50')
    lbl = Label(win,text='Look I clicked the button')
    lbl.pack()

# can change the button size with the help of padx and pady
btn = Button(root,text='Click me',font=('Helvetica',20), padx=20,pady=20,fg='blue', bg='green', command=clickMe)
btn.pack()

root.mainloop()