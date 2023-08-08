from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('First interface')
img = PhotoImage(file='agree.png')
root.iconphoto(False,img)

def again():
    global img
    top = Toplevel()
    top.title('Third interface')
    img = ImageTk.PhotoImage(Image.open('agree.png'))
    lbl = Label(top, image=img).pack()
    lbl = Label(top,text='What the hell, you again!!')
    btn = Button(top,text='Close now',command=top.quit).pack()

def newwindow():
    global img
    top = Toplevel()
    top.title('Third interface')
    img = ImageTk.PhotoImage(Image.open('icon.png'))
    lbl = Label(top, image=img).pack()
    lbl = Label(top,text='What the hell, you again!!')
    btn = Button(top,text='Close now',command=again).pack()

def open():
    global img
    top = Toplevel()
    top.title('Second interface')
    img = ImageTk.PhotoImage(Image.open('apple.png'))
    lbl = Label(top,image=img).pack()
    btn_close = Button(top,text='Open', command=newwindow).pack()

btn = Button(root,text='Second window',command=open)
btn.pack()

root.mainloop()