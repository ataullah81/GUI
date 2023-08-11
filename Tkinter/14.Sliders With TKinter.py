import customtkinter
from tkinter import *

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.geometry('500x500')

vertical = Scale(root, from_=0, to=400, sliderlength=10,length=200)
vertical.pack(padx=10,pady=10)

def slide():
    lbl = customtkinter.CTkLabel(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL,length=300)
horizontal.pack()

lbl = customtkinter.CTkLabel(root, text=horizontal.get()).pack()


btn = customtkinter.CTkButton(root,text='Click Me',command=slide).pack(padx=10,pady=10)
root.mainloop()
