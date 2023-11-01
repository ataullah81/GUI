from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Weather App')
root.geometry('300x300')
img = PhotoImage(file='icon.png')
root.iconphoto(False,img)


root.mainloop()