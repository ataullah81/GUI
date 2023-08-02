from tkinter import *

from PIL import ImageTk,Image

root = Tk()

root.title("Learn python")
#root.iconbitmap('logo.png')
img = PhotoImage(file='icon.png')
root.iconphoto(False, img)

my_img = ImageTk.PhotoImage(Image.open('apple.png'))
my_label = Label(image=my_img) # Same way we can put image on the button
my_label.pack()



btn = Button(root, text='Exit',font=('Helvetica',20),command=root.quit)
btn.pack()

root.mainloop()