from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry()

img = PhotoImage(file='logo.png')
root.iconphoto(False, img)

ent_box = Entry(root, font=('arial',20), width=20, borderwidth=5)
ent_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def btn_click(number):
    #ent_box.delete(0, END)
    current = ent_box.get()
    ent_box.delete(0,END)
    ent_box.insert(0, str(current) + str(number))

def add():
    first_number = ent_box.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    ent_box.delete(0,END)

def sub():
    first_number = ent_box.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    ent_box.delete(0, END)
def multiply():
    first_number = ent_box.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    ent_box.delete(0, END)
def divide():
    first_number = ent_box.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    ent_box.delete(0, END)

def equal():
    second_number = ent_box.get()
    ent_box.delete(0, END)

    if math == 'addition':
        ent_box.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        ent_box.insert(0, f_num - int(second_number))
    elif math == 'multiplication':
        ent_box.insert(0, f_num * int(second_number))
    elif math == 'division':
        ent_box.insert(0, f_num / int(second_number))

def clear():
    ent_box.delete(0, END)

btn_1 = Button(root,text="1",padx=30,pady=20,command=lambda: btn_click(1))
btn_2 = Button(root,text="2",padx=30,pady=20,command=lambda: btn_click(2))
btn_3 = Button(root,text="3",padx=30,pady=20,command=lambda: btn_click(3))
btn_4 = Button(root,text="4",padx=30,pady=20,command=lambda: btn_click(4))
btn_5 = Button(root,text="5",padx=30,pady=20,command=lambda: btn_click(5))
btn_6 = Button(root,text="6",padx=30,pady=20,command=lambda: btn_click(6))
btn_7 = Button(root,text="7",padx=30,pady=20,command=lambda: btn_click(7))
btn_8 = Button(root,text="8",padx=30,pady=20,command=lambda: btn_click(8))
btn_9 = Button(root,text="9",padx=30,pady=20,command=lambda: btn_click(9))
btn_0 = Button(root,text="0",padx=30,pady=20,command=lambda: btn_click(0))
btn_div = Button(root,text="/",padx=32,pady=20,command=divide)
btn_plus = Button(root,text="+",padx=30,pady=20,command=add)
btn_equal = Button(root,text="=",padx=30,pady=20,bg='#64E986',command= equal)
btn_minus = Button(root,text="-",padx=32,pady=20,command=sub)
btn_clear = Button(root,text="Clear",padx=19,pady=20,command = clear)
btn_mul = Button(root,text="x",padx=31,pady=20,command=multiply)





btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
btn_0.grid(row=4,column=1)
btn_div.grid(row=4,column=2)
btn_mul.grid(row=1,column=3)
btn_plus.grid(row=3,column=3)
btn_minus.grid(row=2,column=3)
btn_equal.grid(row=4,column=3)
btn_clear.grid(row=4,column=0)

root.mainloop()
