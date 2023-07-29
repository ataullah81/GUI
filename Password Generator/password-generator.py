from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabetes = string.ascii_lowercase
    capital_alphabetes = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_alphabetes + capital_alphabetes + numbers + special_characters
    password_length = int(lengthBox.get())


    if choice.get() == 1:
        passwordField.insert(0, random.sample(small_alphabetes, password_length))

    elif choice.get() == 2:
        passwordField.insert(0, random.sample(small_alphabetes+capital_alphabetes, password_length))
        
    elif choice.get() == 3:
        passwordField.insert(0, random.sample(all, password_length))

def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()

root.title('PassGen')
root.config(bg='gray10')

choice = IntVar()
Font = ('arial', 13, 'bold')
passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='gray10', fg='white')
passwordLabel.grid(pady=10)

weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradioButton.grid(pady=5)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradioButton.grid(pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradioButton.grid(pady=5)

passwordlengthLabel = Label(root, text='Password Length', font=Font, bg='gray10', fg='white')
passwordlengthLabel.grid()

lengthBox = Spinbox(root, from_=5, to=25, width=5, font=Font)
lengthBox.grid()

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=30, bd=2, font=Font)
passwordField.grid()

copyButton = Button(root, text='Copy', font=Font,command=copy)
copyButton.grid(pady=5)
root.mainloop()
