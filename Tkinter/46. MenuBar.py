import customtkinter
from tkinter import *
from tkcalendar import *
import sqlite3

from tkcalendar import Calendar
from tkinter import ttk


import  sqlite3
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('Menu Bar')
root.geometry("800x600")

my_menu = Menu(root)
root.config(menu=my_menu)

#Create database or connect to one
conn =sqlite3.connect('customer_book.db')

#Create cursor
c = conn.cursor()


#Create table
'''
c.execute("""CREATE TABLE customer (
            customerid integer,
            name text,
            date text,
            info text,
            )""")
'''
#Commit changes
conn.commit()

#Close connection
conn.close()

# Click command
def our_command():
    pass

#File add neew function
def add_new():
    file_add_frame.pack(pady=20, padx= 60, fill='both', expand=True)

    customer_name_lbl = Label(file_add_frame, text='Customer name: ',font=('Helvetica',10),bg='gray')
    customer_name_lbl.grid(row=0, column=1,pady=(10, 0), padx=7,sticky='w')
    customer_name = Entry(file_add_frame, width=50)
    customer_name.grid(row=0, column=2, pady=(10, 0), padx=7,sticky='w')

    customer_date_lbl = Label(file_add_frame, text='Date: ', font=('Helvetica', 10),bg='gray',justify=LEFT)
    customer_date_lbl.grid(row=1, column=1,pady=(10, 0), padx=7,sticky='w')
    customer_date = DateEntry(file_add_frame,date_pattern='dd-mm-yyyy')
    customer_date.grid(row=1, column=2, pady=(10, 0), padx=7,sticky='w')

#Hide all frame function
def hide_all_frame():
    file_add_frame.pack_forget()




#Create a  menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add record",command=add_new)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Create a menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Edit Record",command=our_command)
edit_menu.add_command(label="Delete Record",command=our_command)

# Create a Options item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Find",command=our_command)
option_menu.add_command(label="Find Next",command=our_command)


# Create frame

file_add_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')



root.mainloop()