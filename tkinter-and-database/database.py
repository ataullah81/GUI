from tkinter import *
#from PIL import imageTK, Image
import sqlite3

root = Tk()
root.title('Database connection')
root.geometry('400x400')

# Create a database or connect to one
conn = sqlite3.connect('password_book.db')

# Create cursor
c = conn.cursor()
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('password_book.db')

    # Create cursor
    c = conn.cursor()
    # Insert into table
    c.execute('INSERT INTO password VALUES(:f_name,:password, :env_name)',

              {
                  'f_name': f_name.get(),
                  'password': password.get(),
                  'env_name': env_name.get()
              })
    # Commit
    conn.commit()

    # Close connection
    conn.close()

    # Clear text boxes
    f_name.delete(0,END)
    password.delete(0, END)
    env_name.delete(0, END)
# Create query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('password_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute('SELECT *,oid FROM password')
    records = c.fetchall()
    #print(records)
    #Query through results
    print_username = ''

    for i in records:
        #print_username += str(i[0]) + " " + str(i[1]) + '\n'
        print_username += str(i[0]) + " " +str(i[1]) +  " " + "\t"  +str(i[3]) + '\n'



    #query_label= Label(root,text=print_records)
    #query_label.grid(row=5, column=0, columnspan=2)

    query_text = Text(root, width=20, height=10)
    query_text.grid(row=5, column=0, columnspan=2)
    query_text.insert(1.0,print_username)


    # Commit
    conn.commit()

    # Close connection
    conn.close()

# Database



'''
# Create tables
c.execute("""CREATE TABLE password(
    user_name text,
    password text,
    environment)
    """)
   '''

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, pady=5, padx=20)

password = Entry(root, width=30)
password.grid(row=1, column=1, pady=5, padx=20)

env_name = Entry(root, width=30)
env_name.grid(row=2,column=1, pady=5, padx=20)

f_lb = Label(root,text='User Name:')
f_lb.grid(row=0,column=0,pady=5, padx=10)

password_lb = Label(root,text='Password:')
password_lb.grid(row=1,column=0,pady=5,padx=10)

env_lb = Label(root,text='Environment:')
env_lb.grid(row=2,column=0,pady=5,padx=10)

#Create submit button

submit_button = Button(root, text='Add to database', command=submit)
submit_button.grid(row=3,column=0,columnspan=2, pady=10, padx=10, ipadx=100)

# Create query button
query_btn= Button(root,text='Show Data',command=query)
query_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10, ipadx=100)


# Commit
conn.commit()

# Close connection
conn.close()


root.mainloop()