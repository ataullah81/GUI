
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('First interface')
img = PhotoImage(file='agree.png')
root.iconphoto(False,img)

#root.geometry('300x300')
#Creating frame ¤¤ frame can be without text

#r = IntVar()
#r.set(1)

TOPPINGS = [
    ('Cheese','Cheese'),
    ('Mushroom','Mushroom'),
    ('Onion','Onion'),
    ('Pepperoni','Pepperoni')
]
pizza = StringVar()
pizza.set('Cheese')

for text, topping in TOPPINGS:
    Radiobutton(root,text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()



'''
Radiobutton(root,text='Rahil', variable= r, value=1,command=lambda: clicked(r.get())).pack()
Radiobutton(root,text='Russell', variable= r, value=2,command=lambda: clicked(r.get())).pack()
Radiobutton(root,text='Ataullah', variable= r, value=3,command=lambda: clicked(r.get())).pack()
Radiobutton(root,text='Behesti', variable= r, value=4,command=lambda: clicked(r.get())).pack()
'''
#myLabel = Label(root,text=pizza.get())
#myLabel.pack()

btn = Button(root,text='Click Me', command=lambda : clicked(pizza.get()))
btn.pack()
root.mainloop()