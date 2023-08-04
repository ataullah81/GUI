from tkinter import *


root = Tk()
root.title('First interface')
#root.geometry('300x300')

frame = LabelFrame(root, text='This is a frame.', pady=50, padx=50)
frame.pack(padx=10,pady=10)

btn = Button(frame,text='Exit',command=frame.quit)
btn.pack()

root.mainloop()