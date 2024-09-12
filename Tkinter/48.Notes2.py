import customtkinter
from tkinter import *
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox, filedialog
import sqlite3
import os
import json
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
root.geometry("800x900")

my_menu = Menu(root)
root.config(menu=my_menu)

# Path to settings file
SETTINGS_FILE = 'db_settings.json'


# Function to ask the user for the database directory and name
def ask_database_info():
    def select_directory():
        db_directory = filedialog.askdirectory(title="Select Directory for Database")
        if db_directory:
            directory_label.config(text=f"Directory: {db_directory}")
            return db_directory
        return None

    def submit():
        db_name = db_name_entry.get().strip()
        db_directory = directory_label.cget("text").replace("Directory: ", "").strip()

        if not db_name:
            messagebox.showerror("Input Error", "Please enter a database name.")
            return
        if not db_directory:
            messagebox.showerror("Input Error", "Please select a directory for the database.")
            return

        db_name = db_name + ".db" if not db_name.endswith(".db") else db_name
        db_path = os.path.join(db_directory, db_name)

        # Save database settings
        save_settings(db_path)
        messagebox.showinfo("Success", f"Database path set to: {db_path}")
        db_window.destroy()

        # Now call the function to set up the database after the path is set
        setup_database()

    # Create the Tkinter window for asking database name and directory
    db_window = Toplevel()
    db_window.title("Database Configuration")

    Label(db_window, text="Enter Database Name:").grid(row=0, column=0, padx=10, pady=10)
    db_name_entry = Entry(db_window, width=40)
    db_name_entry.grid(row=0, column=1, padx=10, pady=10)

    select_dir_button = Button(db_window, text="Select Directory", command=select_directory)
    select_dir_button.grid(row=1, column=0, padx=10, pady=10)

    directory_label = Label(db_window, text="Directory: Not selected")
    directory_label.grid(row=1, column=1, padx=10, pady=10)

    submit_button = Button(db_window, text="Submit", command=submit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)


# Function to save connection string to a settings file
def save_settings(db_path):
    settings = {"database_path": db_path}
    with open(SETTINGS_FILE, 'w') as settings_file:
        json.dump(settings, settings_file)


# Function to load database path from settings file
def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as settings_file:
            settings = json.load(settings_file)
            return settings.get("database_path")
    return None


# Function to check if a table exists
def table_exists(cursor, table_name):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    return cursor.fetchone() is not None


# Main function to handle database setup
def setup_database():
    # Load existing database path from settings file
    db_path = load_settings()

    if not db_path:
        # Ask user for database name and directory if settings file doesn't exist
        ask_database_info()
        return  # Exit, database setup will be handled after the user input in `ask_database_info`

    # Check if the database file exists
    if not os.path.exists(db_path):
        # Create the database if it doesn't exist
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Create the table
        c.execute("""CREATE TABLE IF NOT EXISTS customer (
                    name text,
                    subject text,
                    date text,
                    info text,
                    modifydate text
                    )""")

        conn.commit()
        print("Database and table created.")
    else:
        # If the database exists, check for the table
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        if not table_exists(c, "customer"):
            # If the table doesn't exist, create it
            c.execute("""CREATE TABLE customer (
                        name text,
                        subject text,
                        date text,
                        info text,
                        modifydate text
                        )""")
            conn.commit()
            print("Table created in existing database.")
        else:
            print("Table already exists, skipping creation.")

    # Close the connection
    conn.close()


# Call `setup_database` to ensure the database setup occurs after user input
setup_database()

#root.mainloop()


# (Continue with the rest of the functions as in your original script...)


import tkinter as tk
from tkinter import Toplevel, StringVar, Entry, Label, Button, messagebox
from datetime import datetime
import sqlite3


def load_settings():
    # Load the database path from settings file
    if os.path.exists('db_settings.json'):
        with open('db_settings.json', 'r') as settings_file:
            settings = json.load(settings_file)
            return settings.get("database_path")
    return None


def search_window():
    hide_all_frame()

    # Load the database path from settings file
    db_path = load_settings()
    if not db_path:
        messagebox.showerror("Error", "Database path not set. Please configure the database.")
        return

    # Create a new Toplevel window
    global edit_edit_frame
    edit_edit_frame = customtkinter.CTkFrame(master=root, width=800, height=600, fg_color='gray')
    edit_edit_frame.pack(pady=20, padx=60, fill='both', expand=True)

    search_name_var = StringVar()
    search_subject_var = StringVar()

    search_label = Label(edit_edit_frame, text="Enter Customer Name:", font=('Helvetica', 10), bg='gray')
    search_label.grid(row=0, column=0, padx=10, pady=10)
    search_entry = Entry(edit_edit_frame, textvariable=search_name_var, width=50, font=('Helvetica', 10))
    search_entry.grid(row=0, column=1, padx=10, pady=10)

    subject_label = Label(edit_edit_frame, text="Enter Subject:", font=('Helvetica', 10), bg='gray')
    subject_label.grid(row=1, column=0, padx=10, pady=10)
    subject_entry = Entry(edit_edit_frame, textvariable=search_subject_var, width=50, font=('Helvetica', 10))
    subject_entry.grid(row=1, column=1, padx=10, pady=10)

    search_button = Button(edit_edit_frame, text="Search", bg='green',
                           command=lambda: perform_search(search_name_var.get(), search_subject_var.get()))
    search_button.grid(row=0, column=2, padx=10, pady=10)

    def perform_search(customer_name, subject):
        if not customer_name.strip() or not subject.strip():
            messagebox.showwarning("Input Error", "Please enter both customer name and subject.")
            return

        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()

        cur_sor.execute("SELECT * FROM customer WHERE name LIKE ? AND subject LIKE ? COLLATE NOCASE",
                        ('%' + customer_name + '%', '%' + subject + '%'))
        records = cur_sor.fetchall()

        if not records:
            messagebox.showinfo("No Results", "No customer found with that name and subject.")
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
            date_entry.insert(0, record[2])  # Assuming date is in index 2
            notes_entry.delete('1.0', tk.END)
            notes_entry.insert(tk.END, record[3])  # Assuming info is in index 3

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

        # Labels and Entry widgets for editing (using edit_edit_frame instead of win)
        Label(edit_edit_frame, text="Customer Name:", font=('Helvetica', 10), bg='gray').grid(row=2, column=0, padx=10,
                                                                                              pady=5, sticky='e')
        name_entry = Entry(edit_edit_frame, width=50, font=('Helvetica', 10))
        name_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(edit_edit_frame, text="Date:", font=('Helvetica', 10), bg='gray').grid(row=3, column=0, padx=10, pady=5,
                                                                                     sticky='e')
        date_entry = Entry(edit_edit_frame, width=50, font=('Helvetica', 10))
        date_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(edit_edit_frame, text="Notes:", font=('Helvetica', 10), bg='gray').grid(row=9, column=0, padx=10, pady=5,
                                                                                      sticky='ne')
        notes_entry = tk.Text(edit_edit_frame, width=50, height=15, font=('Helvetica', 10))
        notes_entry.grid(row=9, column=1, padx=10, pady=5)

        # Create a Frame to hold both buttons and center them
        button_frame = Frame(edit_edit_frame, bg='gray')
        button_frame.grid(row=10, column=0, columnspan=2, pady=(10, 0), padx=7)

        # Navigation buttons - Previous and Next side by side in the Frame
        prev_button = Button(button_frame, text="Previous", bg='green', command=prev_record, font=('Helvetica', 10))
        next_button = Button(button_frame, text="Next", bg='green', command=next_record, font=('Helvetica', 10))

        prev_button.pack(side=tk.LEFT, padx=10)
        next_button.pack(side=tk.RIGHT, padx=10)

        # Create a label to show the current record index and total records
        status_label = Label(edit_edit_frame, text=f"Record 1 of {total_records}", font=('Helvetica', 10), bg='gray')
        status_label.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        def save_edits():
            conn = sqlite3.connect(db_path)
            cur_sor = conn.cursor()

            # Get the current date and time
            modify_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Update the record in the database with the new values
            cur_sor.execute("""
                UPDATE customer SET 
                    name = ?, 
                    date = ?, 
                    info = ?, 
                    MODIFYDATE = ?
                WHERE name = ? AND subject = ?
            """, (
                name_entry.get(),
                date_entry.get(),
                notes_entry.get("1.0", tk.END).strip(),
                modify_date,
                records[current_record_index][0],  # The original customer name to identify the record
                records[current_record_index][1],  # The original subject to identify the record
            ))

            conn.commit()
            messagebox.showinfo("Success", "Record updated successfully")
            conn.close()

        # Save button to update the record
        save_button = Button(edit_edit_frame, text="Save Changes", command=save_edits, bg='green',
                             font=('Helvetica', 10))
        save_button.grid(row=10, column=1, columnspan=2, pady=(10, 0), padx=7)

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
    #lbl.pack(pady=90, anchor='s')
    lbl.grid(row=0, column=1, pady=(10, 0), padx=20)
    lbl2 = Label(about_window, text='Version 1.1.3',fg='white', bg='#36454F')
    lbl2.grid(row=1, column=1, pady=(10, 0), padx=20)
    #lbl2.pack(pady=90, anchor='w')

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

    btn_query = tk.Button(find_window, text='Show records',bg='green', command=show)
    btn_query.pack(pady=10)

    find_window.mainloop()


def add_new():
    hide_all_frame()
    file_add_frame.pack(pady=20, padx= 60, fill='both', expand=True)

    # create global variables for text boxes
    global customer_name
    global customer_subject
    global customer_date
    global customer_info


    customer_name_lbl = Label(file_add_frame, text='Customer name: ' , font=('Helvetica' ,10),bg='gray')
    customer_name_lbl.grid(row=0, column=1,pady=(10, 0), padx=7,sticky='w')
    customer_name = Entry(file_add_frame, width=50)
    customer_name.grid(row=0, column=2, pady=(10, 0), padx=7,sticky='w')

    customer_subject_lbl = Label(file_add_frame, text='Subject:', font=('Helvetica', 10), bg='gray')
    customer_subject_lbl.grid(row=1, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_subject = Entry(file_add_frame, width=50)
    customer_subject.grid(row=1, column=2, pady=(10, 0), padx=7, sticky='w')

    customer_date_lbl = Label(file_add_frame, text='Date: ', font=('Helvetica', 10),bg='gray',justify=LEFT)
    customer_date_lbl.grid(row=2, column=1,pady=(10, 0), padx=7,sticky='w')
    customer_date = DateEntry(file_add_frame,date_pattern='dd-mm-yyyy')
    customer_date.grid(row=2, column=2, pady=(10, 0), padx=7,sticky='w')

    customer_info_lbl = Label(file_add_frame, text='Notes: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_info_lbl.grid(row=7, column=1, pady=(10, 0), padx=7, sticky='w')
    customer_info = Text(file_add_frame, height=5,width=52)
    customer_info.grid(row=7, column=2, pady=(10, 0), padx=7, sticky='w')

    # Load the database path from settings file


    def submit():
        db_path = load_settings()
        if not db_path:
            messagebox.showerror("Error", "Database path not set. Please configure the database.")
            return

        conn =sqlite3.connect(db_path)
        cursor = conn.cursor()
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            cursor.execute(
                "SELECT name, subject FROM customer WHERE LOWER(name) = LOWER(?) AND LOWER(subject) = LOWER(?)",
                (customer_name.get(), customer_subject.get()))
            if cursor.fetchone():
                messagebox.showerror("Error", "Customer with this subject already exists!")
            else:
                cursor.execute("INSERT INTO customer VALUES (?, ?, ?, ?, ?)",
                               (customer_name.get(), customer_subject.get(), customer_date.get(),
                                customer_info.get("1.0", 'end-1c'), current_date))
                conn.commit()
                messagebox.showinfo("Success", "Record added successfully")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            #Close connection
        finally:
            conn.close()
            customer_name.delete(0, END)
            customer_subject.delete(0, END)
            customer_date.delete(0, END)
            customer_info.delete('1.0', END)

    submit_btn = Button(file_add_frame, text='Save', bg='green', font=('Helvetica', 10), command=submit)
    submit_btn.grid(row=4, column=2, pady=(10, 0), padx=7)
#Hide all frame function
def hide_all_frame():
    file_add_frame.pack_forget()
    edit_edit_frame.pack_forget()
    edit_delete_frame.pack_forget()
    password_frame.pack_forget()
    main_frame.pack_forget()
    show_frame.pack_forget()



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
            info = :notes,
            modifydate = current_date
            WHERE name = :name""",

                        {
                            'name':customer_name.get(),
                            'date':customer_date.get(),
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
        customer_info.delete('1.0', END)
def show():
    hide_all_frame()
    # Load the database path from settings file
    db_path = load_settings()
    if not db_path:
        messagebox.showerror("Error", "Database path not set. Please configure the database.")
        return
    # Check if the user input is empty
    if not z.get().strip():
        messagebox.showwarning("Input Error", "Please enter a customer name.")
        return  # Exit the function if input is empty

    # Create database connection
    conn = sqlite3.connect(db_path)
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
    #show_window = Tk()
    #show_window.title('Show Record')
    #show_window.geometry('600x600')
    global show_frame
    #show_frame = Frame(root)  # Assuming root is your main tkinter window
    show_frame = customtkinter.CTkFrame(master=root, width=800, height=600, fg_color='gray')
    show_frame.pack(pady=20, padx=60, fill='both', expand=True)

    # Create and place widgets to display the customer information
    #main_frame = Frame(show_frame)
    #main_frame.pack(pady=20)

    name_lbl = Label(show_frame, text='Customer name:', font=('Helvetica', 10), justify=LEFT,bg='gray')
    name_lbl.grid(row=0, column=0, pady=(10, 0), padx=7, sticky='e')
    name = Entry(show_frame, width=60)
    name.grid(row=0, column=1, pady=(10, 0), padx=7)


    info_lbl = Label(show_frame, text='Info:',font=('Helvetica', 10),bg='gray')
    info_lbl.grid(row=6, column=0, pady=(10, 0), padx=7, sticky='ne')
    info = Text(show_frame, height=10, width=45)
    info.grid(row=6, column=1, pady=(10, 0), padx=7)

    # Create a Frame to hold navigation buttons (Previous and Next) and center it
    button_frame = Frame(show_frame,bg='gray')
    button_frame.grid(row=7, column=0, columnspan=2, pady=(20, 0))

    # Create Previous and Next buttons side by side in the button frame
    prev_btn = Button(button_frame, text='Previous',bg='green', command=prev_record)
    next_btn = Button(button_frame, text='Next',bg='green', command=next_record)

    prev_btn.pack(side=LEFT, padx=20)
    next_btn.pack(side=RIGHT, padx=20)

    # Create a label to show the current record index and total records, centered
    status_label = Label(show_frame, text=f"Record {current_record_index + 1} of {total_records}",bg='gray')
    status_label.grid(row=8, column=0, columnspan=2, pady=(20, 10))

    # Close button centered below the navigation buttons
    #close = Button(main_frame, text='Exit', command=show_frame.destroy)
    #close.grid(row=9, column=0, columnspan=2, pady=(10, 0))

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

    # Create a listbox to show multiple matching records
    records_listbox = tk.Listbox(edit_delete_frame, height=6, selectmode=tk.SINGLE, width=60)
    records_listbox.grid(row=2, column=2, pady=(10, 0), padx=7)

    def search_records():
        # Load the database path from settings file
        db_path = load_settings()
        if not db_path:
            messagebox.showerror("Error", "Database path not set. Please configure the database.")
            return

        customer_name = y.get()

        if not customer_name:
            messagebox.showwarning("Input Error", "Please enter a customer name.")
            return

        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()

        # Find matching records with a partial search
        cur_sor.execute("SELECT rowid, name, date FROM customer WHERE name LIKE ? COLLATE NOCASE", ('%' + customer_name + '%',))
        records = cur_sor.fetchall()

        # Clear previous listbox entries
        records_listbox.delete(0, tk.END)

        if not records:
            messagebox.showinfo("No Results", "No matching records found.")
            conn.close()
            return

        # Display the records in the listbox
        for record in records:
            records_listbox.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Date: {record[2]}")

        conn.close()

    search_button = tk.Button(edit_delete_frame, text='Search',bg='green', command=search_records)
    search_button.grid(row=0, column=3, padx=10)

    def delete():
        # Load the database path from settings file
        db_path = load_settings()
        if not db_path:
            messagebox.showerror("Error", "Database path not set. Please configure the database.")
            return
        try:
            # Get selected record
            selected_index = records_listbox.curselection()
            if not selected_index:
                messagebox.showwarning("Selection Error", "Please select a record to delete.")
                return

            selected_record = records_listbox.get(selected_index)
            record_id = selected_record.split(",")[0].split(":")[1].strip()  # Extract record ID

            # Confirmation window
            confirm = messagebox.askyesno("Delete Confirmation", f"Are you sure you want to delete record ID {record_id}?")

            if confirm:  # If user clicks "Yes"
                conn = sqlite3.connect(db_path)
                cur_sor = conn.cursor()

                # Delete the record with the selected ID
                cur_sor.execute("DELETE FROM customer WHERE rowid = ?", (record_id,))

                # Commit changes
                conn.commit()

                # Clear the input field and listbox
                del_customer_name.delete(0, tk.END)
                records_listbox.delete(0, tk.END)

                messagebox.showinfo("Success", f"Record ID {record_id} deleted successfully.")

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

        finally:
            # Close connection
            conn.close()

    # Delete record button
    delete_btn = tk.Button(edit_delete_frame, text='Delete',bg='green', command=delete)
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

        special_chars = "!@#$%^&*()_+"
        # You can exclude certain characters here if desired
        allowed_chars = [chr(x) for x in range(33, 127) if chr(x) not in ";:`"]
        # Clear entry box
        pw_entry.delete(0, END)
        # Get password length and convert to integer
        pw_length = int(my_entry.get())
        # create a variable to hold password
        my_password = ''
        '''
        # Loop through password length
        for x in range(pw_length):
            my_password += chr(randint(33, 126))
        '''
        # Generate password
        my_password = ''.join([allowed_chars[randint(0, len(allowed_chars) - 1)] for _ in range(pw_length)])

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
show_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')

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
btn_query = Button(root, text='Show records',bg='green', command=show)
btn_query.pack()
#btn_query = Button(root, text='Search-edit records', command=edit)
#btn_query.pack(pady=10)

search_btn = Button(root, text="Edit Customer",bg='green', command=search_window)
search_btn.pack(pady=20)
#lbl = customtkinter.CTkLabel(root, text='©arbtech')
#lbl.pack(anchor='se')

root.mainloop()