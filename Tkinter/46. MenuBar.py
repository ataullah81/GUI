import customtkinter
from tkinter import *
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox
import sqlite3
import os
from random import randint
import tkinter.messagebox
import tkinter as tk
from tkinter import Toplevel, StringVar, Entry, Button, Label, messagebox
import babel.numbers


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('Customer Info Box')
# Use an absolute path to the icon file
icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
root.iconbitmap(icon_path)
root.geometry("800x600")


my_menu = Menu(root)
root.config(menu=my_menu)

# Define the database name
db_name = 'customer_book.db'

# Function to check if a table exists


def table_exists(cursor, table_name):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    return cursor.fetchone() is not None

# Check if the database file exists


if not os.path.exists(db_name):
    # Create the database if it doesn't exist
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Create the table
    c.execute("""CREATE TABLE customer (
                name text,
                date text,
                link_one text,
                link_two text,
                ftp_link text,
                ftp_username text,
                frp_password text,
                info text,
                modifydate text
                )""")

    conn.commit()
    print("Database and table created.")
else:
    # If the database exists, check for the table
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    if not table_exists(c, "customer"):
        # If the table doesn't exist, create it
        c.execute("""CREATE TABLE customer (
                    name text,
                    date text,
                    link_one text,
                    link_two text,
                    ftp_link text,
                    ftp_username text,
                    frp_password text,
                    info text,
                    modifydate text
                    )""")
        conn.commit()
        print("Table created in existing database.")
    else:
        print("Table already exists, skipping creation.")

# Close the connection
conn.close()

import tkinter as tk
from tkinter import Toplevel, StringVar, Entry, Label, Button, messagebox
from datetime import datetime
import sqlite3

def search_window():
    # Create a new Toplevel window
    search_win = Toplevel()
    search_win.title("Search and Edit Customer")

    # Create a StringVar for the search entry
    search_var = StringVar()

    # Create and place the widgets in the new window
    search_label = Label(search_win, text="Enter Customer Name:", font=('Helvetica', 12))
    search_label.grid(row=0, column=0, padx=10, pady=10)

    search_entry = Entry(search_win, textvariable=search_var, width=30, font=('Helvetica', 12))
    search_entry.grid(row=0, column=1, padx=10, pady=10)

    search_button = Button(search_win, text="Search", command=lambda: perform_search(search_var.get(), search_win))
    search_button.grid(row=0, column=2, padx=10, pady=10)

    def perform_search(customer_name, win):
        if not customer_name.strip():
            messagebox.showwarning("Input Error", "Please enter a customer name.")
            return

        # Connect to the database and perform the search
        conn = sqlite3.connect('customer_book.db')
        cur_sor = conn.cursor()

        cur_sor.execute("SELECT * FROM customer WHERE name LIKE ? COLLATE NOCASE", ('%' + customer_name + '%',))
        records = cur_sor.fetchall()

        if not records:
            messagebox.showinfo("No Results", "No customer found with that name.")
            conn.close()
            return

        global current_record_index
        current_record_index = 0
        total_records = len(records)

        def display_record(index):
            """ Display the customer data in the entry fields """
            record = records[index]
            name_entry.delete(0, tk.END)
            name_entry.insert(0, record[0])
            date_entry.delete(0, tk.END)
            date_entry.insert(0, record[1])
            link1_entry.delete(0, tk.END)
            link1_entry.insert(0, record[2])
            link2_entry.delete(0, tk.END)
            link2_entry.insert(0, record[3])
            ftp_link_entry.delete(0, tk.END)
            ftp_link_entry.insert(0, record[4])
            ftp_username_entry.delete(0, tk.END)
            ftp_username_entry.insert(0, record[5])
            ftp_pass_entry.delete(0, tk.END)
            ftp_pass_entry.insert(0, record[6])
            notes_entry.delete('1.0', tk.END)
            notes_entry.insert(tk.END, record[7])

            # Update the status label to show the current record number and total records
            status_label.config(text=f"Record {index + 1} of {total_records}")

        def next_record():
            """ Show the next record """
            global current_record_index
            if current_record_index < total_records - 1:
                current_record_index += 1
                display_record(current_record_index)

        def prev_record():
            """ Show the previous record """
            global current_record_index
            if current_record_index > 0:
                current_record_index -= 1
                display_record(current_record_index)

        # Labels and Entry widgets for editing
        Label(win, text="Customer Name:", font=('Helvetica', 12)).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        name_entry = Entry(win, width=40, font=('Helvetica', 12))
        name_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(win, text="Date:", font=('Helvetica', 12)).grid(row=3, column=0, padx=10, pady=5, sticky='e')
        date_entry = Entry(win, width=40, font=('Helvetica', 12))
        date_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(win, text="Link TCS2:", font=('Helvetica', 12)).grid(row=4, column=0, padx=10, pady=5, sticky='e')
        link1_entry = Entry(win, width=40, font=('Helvetica', 12))
        link1_entry.grid(row=4, column=1, padx=10, pady=5)

        Label(win, text="Link TCS3:", font=('Helvetica', 12)).grid(row=5, column=0, padx=10, pady=5, sticky='e')
        link2_entry = Entry(win, width=40, font=('Helvetica', 12))
        link2_entry.grid(row=5, column=1, padx=10, pady=5)

        Label(win, text="FTP Link:", font=('Helvetica', 12)).grid(row=6, column=0, padx=10, pady=5, sticky='e')
        ftp_link_entry = Entry(win, width=40, font=('Helvetica', 12))
        ftp_link_entry.grid(row=6, column=1, padx=10, pady=5)

        Label(win, text="FTP Username:", font=('Helvetica', 12)).grid(row=7, column=0, padx=10, pady=5, sticky='e')
        ftp_username_entry = Entry(win, width=40, font=('Helvetica', 12))
        ftp_username_entry.grid(row=7, column=1, padx=10, pady=5)

        Label(win, text="FTP Password:", font=('Helvetica', 12)).grid(row=8, column=0, padx=10, pady=5, sticky='e')
        ftp_pass_entry = Entry(win, width=40, font=('Helvetica', 12))
        ftp_pass_entry.grid(row=8, column=1, padx=10, pady=5)

        Label(win, text="Notes:", font=('Helvetica', 12)).grid(row=9, column=0, padx=10, pady=5, sticky='ne')
        notes_entry = tk.Text(win, width=40, height=4, font=('Helvetica', 12))
        notes_entry.grid(row=9, column=1, padx=10, pady=5)

        # Create a Frame to hold both buttons and center them
        button_frame = Frame(win)
        button_frame.grid(row=11, column=0, columnspan=2)

        # Navigation buttons - Previous and Next side by side in the Frame
        prev_button = Button(button_frame, text="Previous", command=prev_record, font=('Helvetica', 12))
        next_button = Button(button_frame, text="Next", command=next_record, font=('Helvetica', 12))

        prev_button.pack(side=tk.LEFT, padx=10)
        next_button.pack(side=tk.RIGHT, padx=10)

        # Create a label to show the current record index and total records
        status_label = Label(win, text=f"Record 1 of {total_records}", font=('Helvetica', 12))
        status_label.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        def save_edits():
            conn = sqlite3.connect('customer_book.db')
            cur_sor = conn.cursor()

            # Get the current date and time
            modify_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Update the record in the database with the new values
            cur_sor.execute("""
                UPDATE customer SET 
                    name = ?, 
                    date = ?, 
                    link_one = ?, 
                    link_two = ?, 
                    ftp_link = ?, 
                    ftp_username = ?, 
                    frp_password = ?, 
                    info = ?, 
                    MODIFYDATE = ?
                WHERE name = ?
            """, (
                name_entry.get(),
                date_entry.get(),
                link1_entry.get(),
                link2_entry.get(),
                ftp_link_entry.get(),
                ftp_username_entry.get(),
                ftp_pass_entry.get(),
                notes_entry.get("1.0", tk.END).strip(),  # Get the content of the Text widget
                modify_date,  # Set the modify date to the current time
                records[current_record_index][0]  # The original customer name to identify the record
            ))

            conn.commit()
            messagebox.showinfo("Success", "Record updated successfully.")
            conn.close()
            win.destroy()  # Close the search window after saving

        # Save button to update the record
        save_button = Button(win, text="Save Changes", command=save_edits, font=('Helvetica', 12))
        save_button.grid(row=10, column=0, columnspan=2, pady=10)

        # Display the first record by default
        display_record(current_record_index)

        conn.close()

# Assuming the root window is already created and there is a button to call search_window



def our_command():
    pass


def about():
    about_window = Tk()
    about_window.title('About')
    about_window.geometry('300x200')
    lbl = Label(about_window, text='Copyright ©arbrtech. All Rights Reserved', fg='white', bg='#36454F')
    lbl.pack(pady=90, anchor='s')
    # lbl.grid(row=10, column=2, pady=(10, 0), padx=20)

# Find function not in use
def find():
    hide_all_frame()
    find_window = tk.Tk()
    find_window.title('Find Customer')
    find_window.geometry('400x200')  # Specify a reasonable default size

    find_lbl = customtkinter.CTkLabel(find_window, text='Find Customer')
    find_lbl.pack(pady=10)

    find = Entry(find_window, textvariable=z, width=50)
    find.insert(0, 'Enter customer name')
    find.configure(state='disabled')

    def on_click(event):  # This function for placeholder in the entry box
        find.configure(state=NORMAL)
        find.delete(0, END)

    def validate_and_show():
        customer_name = z.get().strip()
        if not customer_name:
            messagebox.showwarning("Input Error", "Please enter a customer name.")
            return
        show()

    find.bind('<Button-1>', on_click)
    find.pack(pady=10)

    btn_query = tk.Button(find_window, text='Show records', command=show)
    btn_query.pack(pady=10)

    find_window.mainloop()


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


    customer_name_lbl = Label(file_add_frame, text='Customer name: ' , font=('Helvetica' ,10),bg='gray')
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
    #customer_info = Entry(file_add_frame, width=70)
    customer_info = Text(file_add_frame, height=5,width=52)
    customer_info.grid(row=7, column=2, pady=(10, 0), padx=7, sticky='w')



    def submit():
        conn =sqlite3.connect('customer_book.db')
        cursor = conn.cursor()
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            #cursor.execute("SELECT name FROM customer where name = ?",(customer_name.get(),))
            cursor.execute("SELECT name FROM customer WHERE LOWER(name) = LOWER(?)", (customer_name.get(),))
            if cursor.fetchone():
                messagebox.showerror("Error", "Customer name already exists!")
            else:
                cursor.execute("INSERT INTO customer VALUES (:name, :date, :link2, :link3, :ftp_link, :ftp_username, :ftp_pass, :notes, :modifydate)",
                            {
                                'name':customer_name.get(),
                                'date':customer_date.get(),
                                'link2':customer_link1.get(),
                                'link3':customer_link2.get(),
                                'ftp_link':customer_ftp_link.get(),
                                'ftp_username':customer_ftp_username.get(),
                                'ftp_pass':customer_ftp_pass.get(),
                                'notes':customer_info.get("1.0",'end-1c'),
                                'modifydate':current_date
                            })
                #Commit changes
                conn.commit()
                messagebox.showinfo("Success", "Record added successfully")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            #Close connection
        finally:
            conn.close()
            #Clear text boxes
            customer_name.delete(0, END)
            customer_date.delete(0,END)
            customer_link1.delete(0,END)
            customer_link2.delete(0,END)
            customer_ftp_link.delete(0,END)
            customer_ftp_username.delete(0,END)
            customer_ftp_pass.delete(0,END)
            customer_info.delete('1.0',END)

    submit_btn = Button(file_add_frame, text='Save',font=('Helvetica', 10),command=submit)
    submit_btn.grid(row=8,column=2,pady=(10, 0), padx=7)
#Hide all frame function
def hide_all_frame():
    file_add_frame.pack_forget()
    edit_edit_frame.pack_forget()
    edit_delete_frame.pack_forget()
    password_frame.pack_forget()
    main_frame.pack_forget()


#Update function
def update():
    conn = sqlite3.connect('customer_book.db')
    # Create cursor
    cur_sor = conn.cursor()
    #record_id = customer_name.get()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:

        cur_sor.execute(""" UPDATE customer SET 
            name= :name,
            date = :date,
            link_one = :link_one,
            link_two = :link_two,
            ftp_link = :ftp_link,
            ftp_username = :ftp_username,
            frp_password = :ftp_pass,
            info = :notes,
            modifydate = current_date
            WHERE name = :name""",

                        {
                            'name':customer_name.get(),
                            'date':customer_date.get(),
                            'link_one':customer_link1.get(),
                            'link_two':customer_link2.get(),
                            'ftp_link':customer_ftp_link.get(),
                            'ftp_username':customer_ftp_username.get(),
                            'ftp_pass':customer_ftp_pass.get(),
                            'notes':customer_info.get("1.0",'end-1c'),
                            'modifydate' :current_date
                            }
                        )


        # Commit changes
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
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
        customer_info.delete('1.0', END)
def show():
    # Check if the user input is empty
    if not z.get().strip():
        messagebox.showwarning("Input Error", "Please enter a customer name.")
        return  # Exit the function if input is empty

    # Create database connection
    conn = sqlite3.connect('customer_book.db')
    # Create cursor
    cur_sor = conn.cursor()

    # Execute the query with the provided customer name (wildcard search)
    cur_sor.execute("SELECT * FROM customer WHERE name LIKE ? COLLATE NOCASE", ('%' + z.get().strip() + '%',))
    records = cur_sor.fetchall()

    if not records:
        messagebox.showinfo("No Records", "No matching records found.")
        conn.close()
        return  # Do not proceed to show window

    global current_record_index
    current_record_index = 0  # Track the index of the current record displayed
    total_records = len(records)  # Get the total number of matching records

    def display_record(record):
        """ Display the customer data in the entry fields """
        name.delete(0, END)
        name.insert(0, record[0])
        link1.delete(0, END)
        link1.insert(0, record[2])
        link2.delete(0, END)
        link2.insert(0, record[3])
        ftp.delete(0, END)
        ftp.insert(0, record[4])
        ftp_user.delete(0, END)
        ftp_user.insert(0, record[5])
        ftp_pass.delete(0, END)
        ftp_pass.insert(0, record[6])
        info.delete('1.0', END)
        info.insert('1.0', record[7])

        # Update the status label to show the current record number and total records
        status_label.config(text=f"Record {current_record_index + 1} of {total_records}")

    def next_record():
        """ Show the next record """
        global current_record_index
        if current_record_index < len(records) - 1:
            current_record_index += 1
            display_record(records[current_record_index])

    def prev_record():
        """ Show the previous record """
        global current_record_index
        if current_record_index > 0:
            current_record_index -= 1
            display_record(records[current_record_index])

    # Create a new window to display the records
    show_window = Tk()
    show_window.title('Show Record')
    show_window.geometry('600x600')

    # Create and place widgets to display the customer information
    main_frame = Frame(show_window)
    main_frame.pack(pady=20)

    name_lbl = Label(main_frame, text='Customer name:')
    name_lbl.grid(row=0, column=0, pady=(10, 0), padx=7, sticky='e')
    name = Entry(main_frame, width=60)
    name.grid(row=0, column=1, pady=(10, 0), padx=7)

    link1_lbl = Label(main_frame, text='Link TCS2:')
    link1_lbl.grid(row=1, column=0, pady=(10, 0), padx=7, sticky='e')
    link1 = Entry(main_frame, width=60)
    link1.grid(row=1, column=1, pady=(10, 0), padx=7)

    link2_lbl = Label(main_frame, text='Link TCS3:')
    link2_lbl.grid(row=2, column=0, pady=(10, 0), padx=7, sticky='e')
    link2 = Entry(main_frame, width=60)
    link2.grid(row=2, column=1, pady=(10, 0), padx=7)

    ftp_lbl = Label(main_frame, text='FTP link:')
    ftp_lbl.grid(row=3, column=0, pady=(10, 0), padx=7, sticky='e')
    ftp = Entry(main_frame, width=60)
    ftp.grid(row=3, column=1, pady=(10, 0), padx=7)

    ftp_user_lbl = Label(main_frame, text='FTP User name:')
    ftp_user_lbl.grid(row=4, column=0, pady=(10, 0), padx=7, sticky='e')
    ftp_user = Entry(main_frame, width=60)
    ftp_user.grid(row=4, column=1, pady=(10, 0), padx=7)

    ftp_pass_lbl = Label(main_frame, text='FTP Password:')
    ftp_pass_lbl.grid(row=5, column=0, pady=(10, 0), padx=7, sticky='e')
    ftp_pass = Entry(main_frame, width=60)
    ftp_pass.grid(row=5, column=1, pady=(10, 0), padx=7)

    info_lbl = Label(main_frame, text='Info:')
    info_lbl.grid(row=6, column=0, pady=(10, 0), padx=7, sticky='ne')
    info = Text(main_frame, height=10, width=45)
    info.grid(row=6, column=1, pady=(10, 0), padx=7)

    # Create a Frame to hold navigation buttons (Previous and Next) and center it
    button_frame = Frame(main_frame)
    button_frame.grid(row=7, column=0, columnspan=2, pady=(20, 0))

    # Create Previous and Next buttons side by side in the button frame
    prev_btn = Button(button_frame, text='Previous', command=prev_record)
    next_btn = Button(button_frame, text='Next', command=next_record)

    prev_btn.pack(side=LEFT, padx=20)
    next_btn.pack(side=RIGHT, padx=20)

    # Create a label to show the current record index and total records, centered
    status_label = Label(main_frame, text=f"Record {current_record_index + 1} of {total_records}")
    status_label.grid(row=8, column=0, columnspan=2, pady=(20, 10))

    # Close button centered below the navigation buttons
    close = Button(main_frame, text='Exit', command=show_window.destroy)
    close.grid(row=9, column=0, columnspan=2, pady=(10, 0))

    # Display the first record by default
    display_record(records[current_record_index])

    # Commit changes and close connection
    conn.commit()
    conn.close()



z = StringVar()
y = StringVar()


def fetch():
    hide_all_frame()

    edit_delete_frame.pack(pady=20, padx=60, fill='both', expand=True)

    customer_name_lbl = tk.Label(edit_delete_frame, text='Customer name: ', font=('Helvetica', 10), bg='gray')
    customer_name_lbl.grid(row=0, column=1, pady=(10, 0), padx=7, sticky='w')

    del_customer_name = tk.Entry(edit_delete_frame, textvariable=y, width=50)
    del_customer_name.insert(0, 'Enter customer name')
    del_customer_name.configure(state='disabled')

    def on_click(event):  # This function for placeholder in entry box
        del_customer_name.configure(state=tk.NORMAL)
        del_customer_name.delete(0, tk.END)

    del_customer_name.bind('<Button-1>', on_click)
    del_customer_name.grid(row=0, column=2, pady=(10, 0), padx=7, sticky='w')

    def delete():
        customer_name = y.get()

        if not customer_name:
            messagebox.showwarning("Input Error", "Please enter a customer name.")
            return

        # Confirmation window
        confirm = messagebox.askyesno("Delete Confirmation",
                                      f"Are you sure you want to delete customer '{customer_name}'?")

        if confirm:  # If user clicks "Yes"
            try:
                conn = sqlite3.connect('customer_book.db')
                cur_sor = conn.cursor()

                # Delete a record with an exact match
                cur_sor.execute("DELETE FROM customer WHERE name = ? COLLATE NOCASE", (customer_name,))  # Exact match

                # Commit changes
                conn.commit()

                # Clear the input field
                del_customer_name.delete(0, tk.END)

                messagebox.showinfo("Success", f"Customer '{customer_name}' deleted successfully.")

            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")

            finally:
                # Close connection
                conn.close()

    # Delete record button
    delete_btn = tk.Button(edit_delete_frame, text='Delete', command=delete)
    delete_btn.grid(row=8, column=2, columnspan=2, pady=10, padx=10, ipadx=95)


def password():
    hide_all_frame()
    # create global variables for text boxes
    #global customer_name
    # If password_frame already has children, destroy them
    for widget in password_frame.winfo_children():
        widget.destroy()

    password_frame.pack(pady=20, padx=60, fill='both', expand=True)

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
        password_frame.clipboard_clear()
        # Copy to clipborad
        password_frame.clipboard_append(pw_entry.get())
        tkinter.messagebox.showinfo('', 'Password copied')

    lf = LabelFrame(password_frame, text='Choose Length of Password',bg='gray')
    lf.pack(pady=20)
    #password_frame.grid(row=0, column=1, pady=(10, 0), padx=7, sticky='w')
    my_entry = Spinbox(lf, from_=5, to=25, font=('Helvetica', 24),bg='gray')
    my_entry.pack(pady=20, padx=20)
    lf2 = LabelFrame(password_frame, text='Generated Password', bd=5,bg='gray')
    lf2.pack()
    # pw_entry = Entry(lf2, text='', font=('Helvetica', 24), bd=0, bg='systembuttonface')
    pw_entry = Entry(lf2, text='', font=('Helvetica', 24), bd=0, bg='gray')
    pw_entry.pack(pady=(0, 20))
    # Label Frame
    # Create our buttons
# Create frame for our buttons
    my_frame = Frame(password_frame,bg='gray')
    my_frame.pack(pady=20)
    my_button = Button(my_frame, text='Generate Strong Password',bg='green', command=random)
    my_button.grid(row=0, column=0, padx=10)

    clip_button = Button(my_frame, text='Copy To Clipboard',bg='green', command=clipping)
    clip_button.grid(row=0, column=1, padx=10)


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
edit_menu.add_command(label="Edit Record",command=search_window)
edit_menu.add_command(label="Delete Record",command=fetch)

# Create a password item
password_menu = Menu(my_menu)
my_menu.add_cascade(label="Password",menu=password_menu)
password_menu.add_command(label="Generate Password",command=password)

# Create a Options item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options",menu=option_menu)
#option_menu.add_command(label="Find",command=find)
#option_menu.add_command(label="Find Next",command=our_command)
option_menu.add_command(label="About",command=about)


# Create frame
main_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='green')
file_add_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')
edit_edit_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')
edit_delete_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')
password_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')

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
#btn_query = Button(root, text='Search-edit records', command=edit)
#btn_query.pack(pady=10)

search_btn = Button(root, text="Edit Customer", command=search_window)
search_btn.pack(pady=20)
lbl = customtkinter.CTkLabel(root, text='©arbtech')
lbl.pack(anchor='se')

root.mainloop()