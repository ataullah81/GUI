from tkinter import *


root = Tk()
root.title('First interface')
#root.geometry('300x300')
#Creating frame ¤¤ frame can be without text
frame = LabelFrame(root, text='This is a frame.', pady=50, padx=50)
frame.pack(padx=10,pady=10)

btn = Button(frame,text='Exit',command=frame.quit)
btn.grid(row=0,column=0)


btn2 = Button(frame,text='Quit',command=frame.quit)
btn2.grid(row=0,column=1)

root.mainloop()