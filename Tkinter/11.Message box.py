from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('First interface')
img = PhotoImage(file='agree.png')
root.iconphoto(False,img)

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno('This is a popup window','Hello guys')
    #Label(root,text=response).pack()
    if response == 1:
        Label(root, text='You clicked yes').pack()
    else:
        Label(root, text='You clicked no').pack()
btn = Button(root,text='Popup',command=popup).pack()


root.mainloop()