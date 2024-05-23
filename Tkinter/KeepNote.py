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

#Update function
def update():
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    cur_sor = conn.cursor()
    record_id = delete_box.get()
    cur_sor.execute(""" UPDATE addresses SET 
        first_name= :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = :oid""",

                    {
                        'first': first_name_editor.get(),
                        'last': last_name_editor.get(),
                        'address': address_editor.get(),
                        'city': city_editor.get(),
                        'state': state_editor.get(),
                        'zipcode': zipcode_editor.get(),
                        'oid': record_id
                        }
                    )


    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
    editor.destroy()

#Edit function
def edit():
    global editor
    editor = Tk()
    editor.title('Edit Record')
    editor.geometry('300x200')
    # Create database connection
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    cur_sor = conn.cursor()

    record_ID = delete_box.get()
    # Query the database
    cur_sor.execute("SELECT * FROM addresses where oid = " + record_ID)
    records = cur_sor.fetchall()

    # create global variables for text boxes
    global first_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor


    # Create text boxes
    first_name_editor = Entry(editor, width=30)
    first_name_editor.grid(row=0, column=1, pady=(10, 0), padx=20)

    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)



    # Create labels
    first_name_lbl = Label(editor, text='First Name: ')
    first_name_lbl.grid(row=0, column=0)

    last_name_lbl = Label(editor, text='Last Name: ')
    last_name_lbl.grid(row=1, column=0)

    address_lbl = Label(editor, text='Address: ')
    address_lbl.grid(row=2, column=0)

    city_lbl = Label(editor, text='City: ')
    city_lbl.grid(row=3, column=0)

    state_lbl = Label(editor, text='State: ')
    state_lbl.grid(row=4, column=0)

    zipcode_lbl = Label(editor, text='Post code: ')
    zipcode_lbl.grid(row=5, column=0)

    # For loop thru retults
    for record in records:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

# Save edited record
    save_btn = Button(editor,text='Save Record', command=update)
    save_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10, ipadx=95)


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
    # clear text boxes
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# Create query function
def show():
    show = Tk()
    show.title('Show Record')
    show.geometry('300x300')
    #Create database connection
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    cur_sor = conn.cursor()

    #Query the database
    cur_sor.execute("SELECT *, oid FROM addresses")
    records = cur_sor.fetchall()
   # print(records)

    # Create query function


    # print(records)

# Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + '\n'
    query_lbl = Label(show, text = print_records)
    query_lbl.grid(row=0,column=2,pady = 10, padx=(100,100))

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()



def showbyid():
    global editor
    editor = Tk()
    editor.title('Edit Record')
    editor.geometry('300x200')
    # Create database connection
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    cur_sor = conn.cursor()

    show_ID = delete_box.get()
    # Query the database
    cur_sor.execute("SELECT * FROM addresses where oid = " + show_ID)
    records = cur_sor.fetchall()

    # create global variables for text boxes
    global first_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor


    # Create text boxes
    first_name_editor = Entry(editor, width=30)
    first_name_editor.grid(row=0, column=1, pady=(10, 0), padx=20)

    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)



    # Create labels
    first_name_lbl = Label(editor, text='First Name: ')
    first_name_lbl.grid(row=0, column=0)

    last_name_lbl = Label(editor, text='Last Name: ')
    last_name_lbl.grid(row=1, column=0)

    address_lbl = Label(editor, text='Address: ')
    address_lbl.grid(row=2, column=0)

    city_lbl = Label(editor, text='City: ')
    city_lbl.grid(row=3, column=0)

    state_lbl = Label(editor, text='State: ')
    state_lbl.grid(row=4, column=0)

    zipcode_lbl = Label(editor, text='Post code: ')
    zipcode_lbl.grid(row=5, column=0)

    # For loop thru retults
    for record in records:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

# Save edited record
    save_btn = Button(editor,text='Exit', command=editor.quit)
    save_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10, ipadx=95)





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

delete_lbl = Label(root,text='Select ID: ')
delete_lbl.grid(row=9,column=0)

# create submit button
btn = Button(root,text='Add record',command=submit)
btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create query button
btn_query = Button(root, text ='Show records', command=show)
btn_query.grid(row=7, column=0,columnspan=2,pady=10, padx=10, ipadx=95)

# create query button by id
btn_query = Button(root, text ='Show records by ID', command=showbyid)
btn_query.grid(row=8, column=0,columnspan=10,pady=10, padx=10, ipadx=95)

#Create a delete button

btn_delete = Button(root,text='Delete Record', command=delete)
btn_delete.grid(row=10,column=0,columnspan=2,pady=10, padx=10, ipadx=95)


#Create and Update Button
btn_update = Button(root,text='Update Record', command=edit)
btn_update.grid(row=11,column=0,columnspan=2,pady=10, padx=10, ipadx=94)
# Commit changes
conn.commit()
#Close connection
conn.close()

root.mainloop()
