from tkinter import *
from random import randint
import tkinter.messagebox

root = Tk()

root.title('Strong Password Generator')
root.geometry('500x300')
root.resizable(0,0)


# Generate random strong password
def random():
    # Clear entry box
    pw_entry.delete(0, END)
    # Get password length and convert to integer
    pw_length = int(my_entry.get())
    # create a variable to hold password
    my_password = ''

    # Loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # Output password to the screen
    pw_entry.insert(0, my_password)


# Copy to clipboard
def clipping():
    # Clear the clipborad
    root.clipboard_clear()
    # Copy to clipborad
    root.clipboard_append(pw_entry.get())
    tkinter.messagebox.showinfo('', 'Password copied')


# Label Frame
lf = LabelFrame(root, text='Choose Length of Password')
lf.pack(pady=20)

# Create Entry box to create designate number of characters
my_entry = Spinbox(lf, from_=5, to=25, font=('Helvetica', 24))
my_entry.pack(pady=20, padx=20)

lf2 = LabelFrame(root, text='Generated Password', bd=5)
lf2.pack()
# Create entry box for our returned password
pw_entry = Entry(lf2, text = '', font=('Helvetica', 24), bd=0, bg='systembuttonface')
pw_entry.pack(pady=(0, 20))

# Create frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our buttons

my_button = Button(my_frame, text='Generate Strong Password', command=random)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text='Copy To Clipboard', command=clipping)
clip_button.grid(row=0, column=1, padx=10)

lbl = Label(root, text='©arb')
lbl.pack(anchor='se')

root.mainloop()
