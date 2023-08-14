import customtkinter
from tkinter import *


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')


root = customtkinter.CTk()
root.geometry('400x300')

def show():
    lbl = customtkinter.CTkLabel(root, text=var.get()).pack()
    if var.get()==1:
        lbl2 = customtkinter.CTkLabel(root,text='You clicked checkbox').pack()
    else:
        lbl2 = customtkinter.CTkLabel(root, text='You uncheck the checkbox').pack()

var = IntVar()
ckBox = customtkinter.CTkCheckBox(root,text='Check this box', variable=var).pack(pady=20)

btn = customtkinter.CTkButton(root, text='Show Selection',command=show).pack()
root.mainloop()