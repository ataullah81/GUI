import sqlite3
from tkinter import *
from PIL import ImageTk,Image
import  sqlite3

root = Tk()
root.title('Database Connection')
root.geometry('300x500')
img = PhotoImage(file='icon.png')
root.iconphoto(False, img)

#Databases
#Create a database or connect to one

conn =sqlite3.connect('address_book.db')

#Create cursor
cur_sor = conn.cursor()
# Create table
'''
cur_sor.execute("""CREATE TABLE addresses(
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer)
""")
'''
# Create function to delete a record
def delete():
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    cur_sor = conn.cursor()
#Delete a record
    cur_sor.execute('DELETE from addresses WHERE oid =' +  delete_box.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
#create submit function for database
def submit():
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    cur_sor = conn.cursor()
    # Create table
    #clear text boxes
    #Insert into table

    conn.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",

                 {
                     'first_name':first_name.get(),
                     'last_name':last_name.get(),
                     'address':address.get(),
                     'city': city.get(),
                     'state': state.get(),
                     'zipcode': zipcode.get()
                 }

                 )


    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# Create query function
def show():
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    cur_sor = conn.cursor()

    #Query the database
    cur_sor.execute("SELECT *, oid FROM addresses")
    records = cur_sor.fetchall()
   # print(records)

# Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + '\n'
    query_lbl = Label(root, text = print_records)
    query_lbl.grid(row=11,column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create text boxes
first_name = Entry(root,width=30)
first_name.grid(row=0,column=1,pady=(10,0), padx=20)

last_name = Entry(root,width=30)
last_name.grid(row=1,column=1, padx=20)

address = Entry(root,width=30)
address.grid(row=2,column=1, padx=20)

city = Entry(root,width=30)
city.grid(row=3,column=1, padx=20)

state = Entry(root,width=30)
state.grid(row=4,column=1, padx=20)

zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1, padx=20)

delete_box = Entry(root,width=30)
delete_box.grid(row=9, column= 1)

# Create labels
first_name_lbl = Label(root,text ='First Name: ')
first_name_lbl.grid(row=0,column=0 )

last_name_lbl = Label(root,text ='Last Name: ')
last_name_lbl.grid(row=1,column=0)

address_lbl = Label(root,text ='Address: ')
address_lbl.grid(row=2,column=0)

city_lbl = Label(root,text ='City: ')
city_lbl.grid(row=3,column=0)

state_lbl = Label(root,text ='State: ')
state_lbl.grid(row=4,column=0)


zipcode_lbl = Label(root,text ='Post code: ')
zipcode_lbl.grid(row=5,column=0)

delete_lbl = Label(root,text='Delete ID: ')
delete_lbl.grid(row=9,column=0)

# create submit button
btn = Button(root,text='Add record',command=submit)
btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create query button
btn_query = Button(root, text ='Show records', command=show)
btn_query.grid(row=7, column=0,columnspan=2,pady=10, padx=10, ipadx=95)
#Create a delete button

btn_delete = Button(root,text='Delete Record', command=delete)
btn_delete.grid(row=10,column=0,columnspan=2,pady=10, padx=10, ipadx=95)

# Commit changes
conn.commit()
#Close connection
conn.close()

root.mainloop()
