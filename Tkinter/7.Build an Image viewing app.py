from tkinter import *

from PIL import ImageTk,Image

root = Tk()
root.title("Learn python")
root.geometry('500x500')
#root.iconbitmap('logo.png')
img = PhotoImage(file='icon.png')
root.iconphoto(False, img)


#Load image
my_img1 = Image.open('picture/img1.jpg')
my_img2 = Image.open('picture/img2.jpg')
my_img3 = Image.open('picture/img3.jpg')
my_img4 = Image.open('picture/img4.jpg')
my_img5 = Image.open('picture/img5.jpg')

#resize images
resize_img1 = my_img1.resize((550,450))
resize_img2 = my_img2.resize((550,450))
resize_img3 = my_img3.resize((550,450))
resize_img4 = my_img4.resize((550,450))
resize_img5 = my_img5.resize((550,450))
#Convert the image
my_img1 = ImageTk.PhotoImage(resize_img1)
my_img2 = ImageTk.PhotoImage(resize_img2)
my_img3 = ImageTk.PhotoImage(resize_img3)
my_img4 = ImageTk.PhotoImage(resize_img4)
my_img5 = ImageTk.PhotoImage(resize_img5)

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

my_label = Label(root,image=my_img1) # Same way we can put image on the button
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    btn_forward = Button(root,text='>>',command=lambda: forward(image_number+1))
    btn_back = Button(root, text='<<', command=lambda: back(image_number-1))

    if image_number ==5:
        btn_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)



def back(image_number):
    global my_label
    global btn_forward
    global btn_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    btn_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    btn_back = Button(root, text='<<', command=lambda: back(image_number-1))

    if image_number == 1:
        btn_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_forward.grid(row=1, column=2)

btn_back = Button(root,text='<<',command=back, state=DISABLED)
btn_exit = Button(root, text='Exit',font=('Helvetica',20),command=root.quit)
btn_forward = Button(root,text='>>',command=lambda: forward(2))
btn_back.grid(row=1,column=0)
btn_exit.grid(row=1,column=1)
btn_forward.grid(row=1,column=2)

root.mainloop()