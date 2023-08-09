from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Open File Dialog box')
img = PhotoImage(file='agree.png')
root.iconphoto(False,img)

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='D:/Python-Class',title='Select a file', filetypes=(('all files','*.*'),('png files','*.png')))
    lbl = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_lbl = Label(image=my_image).pack()

btn = Button(root,text='Open file', command=open).pack()

root.mainloop()