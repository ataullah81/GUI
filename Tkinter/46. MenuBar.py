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
            name text,
            date text,
            link_one text,
            link_two text,
            ftp_link text,
            ftp_username text,
            frp_password text,
            info text
            
            )""")
'''
#Commit changes
conn.commit()

#Close connection
conn.close()

# Create query function
'''
#Create find
def find_customer():
    hide_all_frame()
    global find
    main_frame.pack(pady=20, padx= 60, fill='both', expand=True)
    find_lbl = Label(main_frame,text='Find Customer: ', font=('Helvetica', 10), bg='green')
    find_lbl.grid(row=0,column=0,pady=(10, 0), padx=7, sticky='w')
    #find_lbl.pack()
    find = Entry(main_frame, width=50)
    find.grid(row=0, column=2, pady=(10, 0), padx=7,sticky='w')
    #find_customer.pack()
    # create query button



    btn_query = Button(main_frame, text='Show records', command=show)
    btn_query.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=95)

'''
# Click command
def our_command():
    pass
def about():
    about_window= Tk()
    about_window.title('About')
    about_window.geometry('300x200')
    lbl = Label(about_window, text='Copyright ©arbrtech. All Rights Reserved', fg='white', bg='#36454F')
    lbl.pack(pady=90, anchor='s')
    # lbl.grid(row=10, column=2, pady=(10, 0), padx=20)
def find():
    hide_all_frame()
    find_window=Tk()
    find_window.title('Find customer')
    find_window.geometry()
    find_lbl = customtkinter.CTkLabel(find_window, text='Find Customer')
    find_lbl.pack()
    find = Entry(find_window, textvariable=z, width=50)
    find.insert(0, 'Enter customer name')
    find.configure(state='disabled')

    def on_click(event):  # this function for place holder in entry box
        find.configure(state=NORMAL)
        find.delete(0, END)

    find.bind('<Button-1>', on_click)
    find.pack(pady=10)
    btn_query = Button(find_window, text='Show records', command=show)
    btn_query.pack()
#File add neew function
def add_new():
    hide_all_frame()
    file_add_frame.pack(pady=20, padx= 60, fill='both', expand=True)

    # create global variables for text boxes
    global customer_name
    global customer_date
    global customer_link1
    global customer_link2
    global customer_ftp_link
    global customer_ftp_username
    global customer_ftp_pass
    global customer_info


    customer_name_lbl = Label(file_add_frame, text='Customer name: ',font=('Helvetica',10),bg='gray')
    customer_name_lbl.grid(row=0, column=1,pady=(10, 0), padx=7,sticky='w')
    customer_name = Entry(file_add_frame, width=50)
    customer_name.grid(row=0, column=2, pady=(10, 0), padx=7,sticky='w')

    customer_date_lbl = Label(file_add_frame, text='Date: ', font=('Helvetica', 10),bg='gray',justify=LEFT)
    customer_date_lbl.grid(row=1, column=1,pady=(10, 0), padx=7,sticky='w')
    customer_date = DateEntry(file_add_frame,date_pattern='dd-mm-yyyy')
    customer_date.grid(row=1, column=2, pady=(10, 0), padx=7,sticky='w')

    customer_link1_lbl = Label(file_add_frame, text='Link TCS2: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_link1_lbl.grid(row=2, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_link1 = Entry(file_add_frame, width=70)
    customer_link1.grid(row=2, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_link2_lbl = Label(file_add_frame, text='Link TCS3: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_link2_lbl.grid(row=3, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_link2 = Entry(file_add_frame, width=70)
    customer_link2.grid(row=3, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_ftp_link_lbl = Label(file_add_frame, text='FTP Link: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_ftp_link_lbl.grid(row=4, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_ftp_link = Entry(file_add_frame, width=70)
    customer_ftp_link.grid(row=4, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_ftp_username_lbl = Label(file_add_frame, text='FTP username: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_ftp_username_lbl.grid(row=5, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_ftp_username = Entry(file_add_frame, width=70)
    customer_ftp_username.grid(row=5, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_ftp_pass_lbl = Label(file_add_frame, text='FTP password: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_ftp_pass_lbl.grid(row=6, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_ftp_pass = Entry(file_add_frame, width=70)
    customer_ftp_pass.grid(row=6, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_info_lbl = Label(file_add_frame, text='Notes: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_info_lbl.grid(row=7, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_info = Entry(file_add_frame, width=70)
    customer_info.grid(row=7, column=2, pady=(10, 0), padx=7, sticky='w')



    def submit():
        conn =sqlite3.connect('customer_book.db')
        conn.execute("INSERT INTO customer VALUES (:name, :date, :link2, :link3, :ftp_link, :ftp_username, :ftp_pass, :notes)",
                    {
                        'name':customer_name.get(),
                        'date':customer_date.get(),
                        'link2':customer_link1.get(),
                        'link3':customer_link2.get(),
                        'ftp_link':customer_ftp_link.get(),
                        'ftp_username':customer_ftp_username.get(),
                        'ftp_pass':customer_ftp_pass.get(),
                        'notes':customer_info.get()
                    }

                     )
        #Commit changes
        conn.commit()
        #Close connection
        conn.close()
        #Clear text boxes
        customer_name.delete(0, END)
        customer_date.delete(0,END)
        customer_link1.delete(0,END)
        customer_link2.delete(0,END)
        customer_ftp_link.delete(0,END)
        customer_ftp_username.delete(0,END)
        customer_ftp_pass.delete(0,END)
        customer_info.delete(0,END)

    submit_btn = Button(file_add_frame, text='Save',font=('Helvetica', 10),command=submit)
    submit_btn.grid(row=8,column=2,pady=(10, 0), padx=7)
#Hide all frame function
def hide_all_frame():
    file_add_frame.pack_forget()
    edit_edit_frame.pack_forget()
    main_frame.pack_forget()

#Update function
def update():
    conn = sqlite3.connect('customer_book.db')
    # Create cursor
    cur_sor = conn.cursor()
    record_id = customer_name.get()
    cur_sor.execute(""" UPDATE customer SET 
        name= :name,
        date = :date,
        link_one = :link_one,
        link_two = :link_two,
        ftp_link = :ftp_link,
        ftp_username = :ftp_username,
        frp_password = :ftp_pass,
        info = :notes
        WHERE name = :name""",

                    {
                        'name':customer_name.get(),
                        'date':customer_date.get(),
                        'link_one':customer_link1.get(),
                        'link_two':customer_link2.get(),
                        'ftp_link':customer_ftp_link.get(),
                        'ftp_username':customer_ftp_username.get(),
                        'ftp_pass':customer_ftp_pass.get(),
                        'notes':customer_info.get()
                        }
                    )


    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
    #editor.destroy()
    # Clear text boxes
    customer_name.delete(0, END)
    customer_date.delete(0, END)
    customer_link1.delete(0, END)
    customer_link2.delete(0, END)
    customer_ftp_link.delete(0, END)
    customer_ftp_username.delete(0, END)
    customer_ftp_pass.delete(0, END)
    customer_info.delete(0, END)

def edit():
    hide_all_frame()
    # create global variables for text boxes
    global customer_name
    global customer_date
    global customer_link1
    global customer_link2
    global customer_ftp_link
    global customer_ftp_username
    global customer_ftp_pass
    global customer_info
    edit_edit_frame.pack(pady=20, padx=60, fill='both', expand=True)

    customer_name_lbl = Label(edit_edit_frame, text='Customer name: ', font=('Helvetica', 10), bg='gray')
    customer_name_lbl.grid(row=0, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_name = Entry(edit_edit_frame, width=50)
    customer_name.grid(row=0, column=2, pady=(10, 0), padx=7, sticky='w')


    # Create database connection
    conn = sqlite3.connect('customer_book.db')
    # Create cursor
    cur_sor = conn.cursor()

    #record_ID = customer_name.get()
    # Query the database
    #cur_sor.execute("SELECT * FROM addresses where oid = " + record_ID)
    cur_sor.execute("SELECT * FROM customer where name like ?COLLATE NOCASE", ('%' + z.get() + '%',))
    records = cur_sor.fetchall()



    # Create text boxes


    customer_date_lbl = Label(edit_edit_frame, text='Date: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_date_lbl.grid(row=1, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_date = DateEntry(edit_edit_frame, date_pattern='dd-mm-yyyy')
    customer_date.grid(row=1, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_link1_lbl = Label(edit_edit_frame, text='Link TCS2: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_link1_lbl.grid(row=2, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_link1 = Entry(edit_edit_frame, width=70)
    customer_link1.grid(row=2, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_link2_lbl = Label(edit_edit_frame, text='Link TCS3: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_link2_lbl.grid(row=3, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_link2 = Entry(edit_edit_frame, width=70)
    customer_link2.grid(row=3, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_ftp_link_lbl = Label(edit_edit_frame, text='FTP Link: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_ftp_link_lbl.grid(row=4, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_ftp_link = Entry(edit_edit_frame, width=70)
    customer_ftp_link.grid(row=4, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_ftp_username_lbl = Label(edit_edit_frame, text='FTP username: ', font=('Helvetica', 10), bg='gray',
                                      justify=LEFT)
    customer_ftp_username_lbl.grid(row=5, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_ftp_username = Entry(edit_edit_frame, width=70)
    customer_ftp_username.grid(row=5, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_ftp_pass_lbl = Label(edit_edit_frame, text='FTP password: ', font=('Helvetica', 10), bg='gray',
                                  justify=LEFT)
    customer_ftp_pass_lbl.grid(row=6, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_ftp_pass = Entry(edit_edit_frame, width=70)
    customer_ftp_pass.grid(row=6, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_info_lbl = Label(edit_edit_frame, text='Notes: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_info_lbl.grid(row=7, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_info = Entry(edit_edit_frame, width=70)
    customer_info.grid(row=7, column=2, pady=(10, 0), padx=7, sticky='w')

    # For loop thru retults
    for record in records:
        customer_name.insert(0, record[0])
        # customer_date.insert(0,record[1])
        customer_link1.insert(0, record[2])
        customer_link2.insert(0, record[3])
        customer_ftp_link.insert(0, record[4])
        customer_ftp_username.insert(0, record[5])
        customer_ftp_pass.insert(0, record[6])
        customer_info.insert(0, record[7])



    # Save edited record
    save_btn = Button(edit_edit_frame, text='Save Record', command=update)
    save_btn.grid(row=8, column=2, columnspan=2, pady=10, padx=10, ipadx=95)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


   # print(records)

    # Create query function
def show():
    global find
    show = Tk()
    show.title('Show Record')
    show.geometry('600x600')
    # Create database connection
    conn = sqlite3.connect('customer_book.db')
        # Create cursor
    cur_sor = conn.cursor()

    #customer_name = find.get()
    # Query the database
    #cur_sor.execute("SELECT *, oid FROM customer")
    cur_sor.execute("SELECT * FROM customer where name like ?COLLATE NOCASE", ('%' + z.get() + '%',)) # % used to find customer information with wild card search
    records = cur_sor.fetchall()



    # print(records)
    name_lbl = Label(show, text='Customer name:')
    name_lbl.grid(row=0, column=1, pady=(10, 0), padx=7,sticky='w')
    name = Entry(show, width=60)
    name.grid(row=0, column=2, pady=(10, 0), padx=7,sticky='w')
    '''
    date_lbl = Label(show, text='Date:')
    date_lbl.grid(row=1, column=1, pady=(10, 0), padx=7,sticky='w')
    date = Entry(show, width=50)
    date.grid(row=1, column=2, pady=(10, 0), padx=7,sticky='w')
    '''
    link1_lbl = Label(show, text='Link TCS2:')
    link1_lbl.grid(row=2, column=1, pady=(10, 0), padx=7,sticky='w')
    link1 = Entry(show, width=60)
    link1.grid(row=2, column=2, pady=(10, 0), padx=7,sticky='w')

    link2_lbl = Label(show, text='Link TCS3:')
    link2_lbl.grid(row=3, column=1, pady=(10, 0), padx=7,sticky='w')
    link2 = Entry(show, width=60)
    link2.grid(row=3, column=2, pady=(10, 0), padx=7,sticky='w')

    ftp_lbl = Label(show, text='FTP link:')
    ftp_lbl.grid(row=4, column=1, pady=(10, 0), padx=7, sticky='w')
    ftp = Entry(show, width=60)
    ftp.grid(row=4, column=2, pady=(10, 0), padx=7, sticky='w')

    ftp_user_lbl = Label(show, text='FTP User name:')
    ftp_user_lbl.grid(row=5, column=1, pady=(10, 0), padx=7, sticky='w')
    ftp_user = Entry(show, width=60)
    ftp_user.grid(row=5, column=2, pady=(10, 0), padx=7, sticky='w')

    ftp_pass_lbl = Label(show, text='FTP Password:')
    ftp_pass_lbl.grid(row=6, column=1, pady=(10, 0), padx=7, sticky='w')
    ftp_pass = Entry(show, width=60)
    ftp_pass.grid(row=6, column=2, pady=(10, 0), padx=7, sticky='w')

    info_lbl = Label(show, text='Info:')
    info_lbl.grid(row=7, column=1, pady=(10, 0), padx=7, sticky='w')
    info =Entry(show,width=60)
    #info.grid(row=7, column=2, pady=(10, 0), padx=7, sticky='w')
    info.grid(row=7, column=2, pady=(10, 0),ipady=20, padx=7, sticky='w')

    close = Button(show, text='Exit', command = show.destroy)
    close.grid(row=10, column=2, pady=(10, 0), padx=20)

    for record in records:
        name.insert(0,record[0])
        #date.insert(0,record[1])
        link1.insert(0,record[2])
        link2.insert(0,record[3])
        ftp.insert(0,record[4])
        ftp_user.insert(0,record[5])
        ftp_pass.insert(0,record[6])
        info.insert(0,record[7])

    '''
# Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) +'\n' " " + str(record[2]) + '\n' " " + str(record[1]) + str(record[3]) + str(record[4]) +str(record[5])  +"\t" + str(record[7]) + '\n'
    query_lbl = Label(show, text = print_records)
    query_lbl.grid(row=0,column=2,pady = 10, padx=(100,100))
    '''
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

z = StringVar()


#Create a  menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
#file_menu.add_command(label="Main Window",command=find_customer)
file_menu.add_separator()
file_menu.add_command(label="Add record",command=add_new)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Create a menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Edit Record",command=edit)
edit_menu.add_command(label="Delete Record",command=our_command)

# Create a Options item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Find",command=find)
#option_menu.add_command(label="Find Next",command=our_command)
option_menu.add_command(label="About",command=about)






# Create frame
main_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='green')
file_add_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')
edit_edit_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')

find_lbl = customtkinter.CTkLabel(root,text = 'Find Customer')
find_lbl.pack()
find = Entry(root,textvariable=z, width=50)
find.insert(0,'Enter customer name')
find.configure(state='disabled')
def on_click(event):  # this function for place holder in entry box
    find.configure(state=NORMAL)
    find.delete(0,END)
find.bind('<Button-1>',on_click)
find.pack(pady=10)
btn_query = Button(root, text='Show records', command=show)
btn_query.pack()
btn_query = Button(root, text='Edit records', command=edit)
btn_query.pack(pady=10)

'''
lbl = Label(root, text='©arbrtech',fg='white',bg='#36454F')
lbl.pack(pady=235,anchor='s')
#lbl.grid(row=10, column=2, pady=(10, 0), padx=20)
'''
'''
find_lbl = customtkinter.CTkLabel(root,text='Find Customer: ', font=('Helvetica', 20))
find_lbl.grid(row=0,column=0,pady=(10, 0), padx=7, sticky='w')
find = Entry(root, width=50)
find.grid(row=0, column=2, pady=(10, 0), padx=7,sticky='w')
btn_query = Button(root, text='Show records', command=show)
btn_query.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=95)
'''
root.mainloop()