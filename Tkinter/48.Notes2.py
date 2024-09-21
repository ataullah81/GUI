import customtkinter
from tkinter import *

from customtkinter import *
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox, filedialog
import sqlite3
import os
import json
from random import randint
import tkinter.messagebox
import bcrypt  # Library for password hashing
import tkinter as tk
from tkinter import Toplevel, StringVar, Entry, Button, Label, messagebox
import babel.numbers


def CenterDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width / 2) - (width / 2)) * scale_factor)
    y = int(((screen_height / 2) - (height / 1.9)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Initialize the main window
root = customtkinter.CTk()
#root.title('Ticket Info Box')
root.geometry(CenterDisplay(root, 900, 950))
root.title("Ticket Info Box")
icon_path = os.path.join(os.path.dirname(__file__), 'report.ico')
root.iconbitmap(icon_path)
root.geometry("800x900")
#Label(root, text="Welcome to the main application").pack(pady=20)

my_menu = Menu(root)
root.config(menu=my_menu)

# Path to settings file
SETTINGS_FILE = 'db_settings.json'


# Database setup function to create users and customer tables
def setup_database():
    # Load existing database path from settings file
    db_path = load_settings()

    if not db_path:
        # Ask user for database name and directory if settings file doesn't exist
        ask_database_info()
        return  # Exit, database setup will be handled after the user input in `ask_database_info`

    # Check if the database file exists
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create the users table (for login)
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
                )""")

    # Create the customer table (your original program)
    c.execute("""CREATE TABLE IF NOT EXISTS customer (
                name TEXT,
                subject TEXT,
                date TEXT,
                info TEXT,
                modifydate TEXT
                )""")

    # Add a default admin user if no users exist
    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] == 0:
        hashed_password = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt())
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", hashed_password))
        conn.commit()

    conn.close()


# Function to load database path from settings file
def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as settings_file:
            settings = json.load(settings_file)
            return settings.get("database_path")
    return None


# Function to ask for the database info
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
    db_window.wm_attributes("-topmost", 1)

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


# Login window
def login_window():
    login = Toplevel()
    login.title("Login")
    login.geometry(CenterDisplay(login, 400, 250))

    Label(login, text="Username:").pack(pady=10)
    username_entry = customtkinter.CTkEntry(login, width=250)
    username_entry.pack(pady=5)

    Label(login, text="Password:").pack(pady=10)
    password_entry = customtkinter.CTkEntry(login, width=250, show='*')
    password_entry.pack(pady=5)

    admin_user = "admin"  # Define the admin username

    def authenticate():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        db_path = load_settings()
        if not db_path:
            messagebox.showerror("Error", "Database path not set. Please configure the database.")
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result and bcrypt.checkpw(password.encode(), result[0]):
            messagebox.showinfo("Login Success", "You have logged in successfully.")
            login.destroy()  # Close the login window
            root.deiconify()  # Show the main window

            # Check if the logged-in user is the admin
            if username == admin_user:
                # Only add the "User Management" menu if the user is admin
                my_menu.add_cascade(label="User Management", menu=user_menu)
                user_menu.add_command(label="Add User", command=add_user_window)
                user_menu.add_command(label="Delete User", command=delete_user_window)  # Add the Delete User option
                user_menu.add_command(label="Edit User", command=edit_user_window)  # Add the Edit User option
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    '''
    def authenticate():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        db_path = load_settings()
        if not db_path:
            messagebox.showerror("Error", "Database path not set. Please configure the database.")
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result and bcrypt.checkpw(password.encode(), result[0]):
            messagebox.showinfo("Login Success", "You have logged in successfully.")
            login.destroy()  # Close the login window
            root.deiconify()  # Show the main window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
'''
    Button(login, text="Login", command=authenticate).pack(pady=20)



root.withdraw()  # Hide the main window
# First, setup the database if it's not set
setup_database()
login_window()   # Show the login window
#root.mainloop()  # Start the main event loop


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

    # Create the main frame for the search window
    global edit_edit_frame
    edit_edit_frame = customtkinter.CTkFrame(master=root, width=800, height=600, fg_color='gray')
    edit_edit_frame.pack(pady=20, padx=60, fill='both', expand=True)
    edit_edit_frame.grid_columnconfigure(1, weight=1) # The second column (index 1) has more weight
    # Function to load all distinct customer names from the database
    def load_customer_names():
        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()
        cur_sor.execute("SELECT DISTINCT name FROM customer")
        customer_names = cur_sor.fetchall()
        conn.close()
        return [name[0] for name in customer_names]

    # Function to load all subjects for a selected customer
    def load_subjects(customer_name):
        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()
        cur_sor.execute("SELECT DISTINCT subject FROM customer WHERE name LIKE ? COLLATE NOCASE", ('%' + customer_name + '%',))
        subjects = cur_sor.fetchall()
        conn.close()
        return [subject[0] for subject in subjects]

    # Function to filter subjects dynamically based on user input
    def filter_subjects(search_term, customer_name):
        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()
        cur_sor.execute(
            "SELECT DISTINCT subject FROM customer WHERE name = ? AND subject LIKE ? COLLATE NOCASE",
            (customer_name, '%' + search_term + '%')
        )
        filtered_subjects = cur_sor.fetchall()
        conn.close()
        return [subject[0] for subject in filtered_subjects]

    # Load the customer names into the dropdown menu
    customer_names_list = load_customer_names()

    if not customer_names_list:
        messagebox.showinfo("No Data", "No customers found in the database.")
        return

    # Customer Name Dropdown Menu
    customer_name_var = StringVar(edit_edit_frame)
    customer_name_var.set(customer_names_list[0])

    customer_label = CTkLabel(edit_edit_frame, text="Select Customer Name:", font=('Helvetica', 15))
    customer_label.grid(row=0, column=0, padx=10, pady=10)

    customer_dropdown = customtkinter.CTkOptionMenu(edit_edit_frame, width=250, values=customer_names_list, variable=customer_name_var)
    customer_dropdown.grid(row=0, column=1, padx=(10,0), pady=10, sticky="nsew")

    # Subject Dropdown Menu (Initially empty until customer is selected)
    subject_var = StringVar(edit_edit_frame)

    subject_label = CTkLabel(edit_edit_frame, text="Select Subject:", font=('Helvetica', 15) )
    subject_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    subject_dropdown = customtkinter.CTkOptionMenu(edit_edit_frame, width=250, values=[], variable=subject_var)
    subject_dropdown.grid(row=1, column=1, padx=(10,0), pady=10, sticky="nsew")

    # Subject Search Box
    subject_search_var = StringVar()

    subject_search_label = CTkLabel(edit_edit_frame, text="Search Subject:", font=('Helvetica', 15))
    subject_search_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

    subject_search_entry = CTkEntry(edit_edit_frame, textvariable=subject_search_var, width=250, font=('Helvetica', 15))
    subject_search_entry.grid(row=2, column=1, padx=(10,0), pady=5, sticky="nsew")

    # Function to update the subjects dropdown based on the selected customer and search term
    def update_subjects_dropdown(selected_customer_name):
        subjects_list = load_subjects(selected_customer_name)
        if subjects_list:
            subject_var.set(subjects_list[0])  # Set the first subject as default
            subject_dropdown.configure(values=subjects_list)
        else:
            subject_var.set('')  # Clear the dropdown if no subjects are found
            subject_dropdown.configure(values=[])

    # Function to update subjects based on search input
    def update_subject_search(event):
        search_term = subject_search_var.get()
        selected_customer_name = customer_name_var.get()
        filtered_subjects = filter_subjects(search_term, selected_customer_name)
        if filtered_subjects:
            subject_var.set(filtered_subjects[0])  # Set the first subject as default
            subject_dropdown.configure(values=filtered_subjects)
        else:
            subject_var.set('')  # Clear the dropdown if no subjects are found
            subject_dropdown.configure(values=[])

    # Bind the subject search box to dynamically update the subject dropdown as the user types
    subject_search_entry.bind("<KeyRelease>", update_subject_search)

    # Update subjects when a customer is selected
    customer_dropdown.configure(command=lambda _: update_subjects_dropdown(customer_name_var.get()))

    # Load subjects for the default customer when the window opens
    update_subjects_dropdown(customer_name_var.get())

    # Search button to perform search based on selected customer and subject
    search_button = CTkButton(edit_edit_frame, text="Search",
                           command=lambda: perform_search(customer_name_var.get(), subject_var.get()))
    search_button.grid(row=2, column=2, padx=10, pady=10)

    # Define global entry fields here so they can be accessed throughout
    global name_entry, subject_entry, date_entry, notes_entry

    # Entry fields for editing (defined outside perform_search so accessible globally)
    CTkLabel(edit_edit_frame, text="Customer Name:", font=('Helvetica', 15)).grid(row=3, column=0, padx=10, pady=5, sticky='e')
    name_entry = CTkEntry(edit_edit_frame, width=250, font=('Helvetica', 15))
    name_entry.grid(row=3, column=1, padx=(10,0), pady=5, sticky="nsew")

    CTkLabel(edit_edit_frame, text="Subject:", font=('Helvetica', 15)).grid(row=4, column=0, padx=10, pady=5, sticky='e')
    subject_entry = CTkEntry(edit_edit_frame, width=350, font=('Helvetica', 15))
    subject_entry.grid(row=4, column=1, padx=(10,0), pady=5, sticky="nsew")

    CTkLabel(edit_edit_frame, text="Date:", font=('Helvetica', 15)).grid(row=5, column=0, padx=10, pady=5, sticky='e')
    date_entry = CTkEntry(edit_edit_frame, width=350, font=('Helvetica', 15))
    date_entry.grid(row=5, column=1, padx=(10,0), pady=5, sticky="nsew")

    CTkLabel(edit_edit_frame, text="Notes:", font=('Helvetica', 15)).grid(row=6, column=0, padx=10, pady=5, sticky='e')
    notes_entry = CTkTextbox(edit_edit_frame, width=350, height=400, font=('Helvetica', 15))
    notes_entry.grid(row=6, column=1, padx=(10,0), pady=5, sticky="nsew")

    # Success message label (initially empty)
    success_label = CTkLabel(edit_edit_frame, text="", font=('Helvetica', 10))
    success_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

    # Track changes and autosave every 10 seconds
    change_detected = False
    auto_save_timer = None

    # Mark changes as detected
    def on_change(*args):
        nonlocal change_detected
        change_detected = True
        reset_auto_save_timer()

    # Reset the timer for auto-saving
    def reset_auto_save_timer():
        nonlocal auto_save_timer
        if auto_save_timer:
            edit_edit_frame.after_cancel(auto_save_timer)  # Cancel the existing timer if present
        auto_save_timer = edit_edit_frame.after(10000, auto_save_changes)  # Set the timer to 10 seconds

    # Perform search function
    def perform_search(customer_name, subject):
        if not customer_name.strip() or not subject.strip():
            messagebox.showwarning("Input Error", "Please select both customer name and subject.")
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
            subject_entry.delete(0, tk.END)
            subject_entry.insert(0, record[1])
            date_entry.delete(0, tk.END)
            date_entry.insert(0, record[4])
            notes_entry.delete('1.0', tk.END)
            notes_entry.insert(tk.END, record[3])

            status_label.configure(text=f"Record {index + 1} of {total_records}")

        def next_record():
            global current_record_index
            if current_record_index < total_records - 1:
                current_record_index += 1
                display_record(current_record_index)

        def prev_record():
            global current_record_index
            if current_record_index > 0:
                current_record_index -= 1
                display_record(current_record_index)


        status_label = Label(edit_edit_frame, text=f"Record 1 of {total_records}", font=('Helvetica', 10), bg='gray')
        status_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        display_record(current_record_index)
        conn.close()

    # Save changes automatically every 10 seconds if changes are detected
    def auto_save_changes():
        nonlocal change_detected
        if change_detected:
            save_edits()
            change_detected = False
        reset_auto_save_timer()

    # Save changes function
    def save_edits():
        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()
        modify_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
            name_entry.get(),
            subject_entry.get(),
        ))
        conn.commit()
        conn.close()

        # Update success label
        success_label.configure(text="Record updated successfully")

        # Automatically hide the label after 3 seconds
        edit_edit_frame.after(3000, hide_success_label)

        # Function to hide the success label

    def hide_success_label():
        success_label.configure(text="")

    # Attach change tracking to each input field
    name_entry_var = tk.StringVar()
    subject_entry_var = tk.StringVar()
    date_entry_var = tk.StringVar()

    name_entry_var.trace_add('write', on_change)
    subject_entry_var.trace_add('write', on_change)
    date_entry_var.trace_add('write', on_change)
    notes_entry.bind('<KeyRelease>', on_change)

    # Reset the timer for auto-saving changes
    reset_auto_save_timer()


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


def add_new():
    hide_all_frame()
    file_add_frame.pack(pady=20, padx=60, fill='both', expand=True)

    global customer_name_dropdown
    global customer_subject
    global customer_date
    global customer_info

    # Function to load all distinct customer names
    def load_customer_names():
        db_path = load_settings()
        if not db_path:
            messagebox.showerror("Error", "Database path not set. Please configure the database.")
            return []

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT name FROM customer")
        customer_names = cursor.fetchall()
        conn.close()

        # Flatten the list of customer names
        return [name[0] for name in customer_names]

    # Load the customer names into the dropdown menu
    customer_names_list = load_customer_names()

    customer_name_lbl = Label(file_add_frame, text='Select or Add Customer:', font=('Helvetica', 10), bg='gray')
    customer_name_lbl.grid(row=0, column=1, pady=(10, 0), padx=7, sticky='e')

    customer_name_var = StringVar(file_add_frame)

    # Combining dropdown and entry for customer name
    if customer_names_list:
        customer_name_var.set("Select or Add Customer")
        customer_name_dropdown = customtkinter.CTkOptionMenu(file_add_frame, values=customer_names_list,
                                                             variable=customer_name_var)
        customer_name_dropdown.grid(row=0, column=2, pady=(10, 0), padx=7, sticky='w')
    else:
        customer_name_var.set("Add New Customer")

    # Entry field to allow adding a new customer even when customers are available
    customer_name_entry = Entry(file_add_frame, textvariable=customer_name_var, width=50)
    customer_name_entry.grid(row=1, column=2, pady=(10, 0), padx=7, sticky='w')

    # New subject input
    customer_subject_lbl = Label(file_add_frame, text='New Subject:', font=('Helvetica', 10), bg='gray')
    customer_subject_lbl.grid(row=2, column=1, pady=(10, 0), padx=7, sticky='e')
    customer_subject = Entry(file_add_frame, width=50)
    customer_subject.grid(row=2, column=2, pady=(10, 0), padx=7, sticky='w')

    # Date input
    customer_date_lbl = Label(file_add_frame, text='Date: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_date_lbl.grid(row=3, column=1, pady=(10, 0), padx=7, sticky='e')
    customer_date = DateEntry(file_add_frame, date_pattern='dd-mm-yyyy')
    customer_date.grid(row=3, column=2, pady=(10, 0), padx=7, sticky='w')

    # Notes input
    customer_info_lbl = Label(file_add_frame, text='Notes: ', font=('Helvetica', 10), bg='gray', justify=LEFT)
    customer_info_lbl.grid(row=4, column=1, pady=(10, 0), padx=7, sticky='e')
    customer_info = Text(file_add_frame, height=25, width=52)
    customer_info.grid(row=4, column=2, pady=(10, 0), padx=7, sticky='w')

    # Submit new subject for the selected or new customer
    def submit():
        db_path = load_settings()
        if not db_path:
            messagebox.showerror("Error", "Database path not set. Please configure the database.")
            return

        selected_customer_name = customer_name_var.get().strip()
        subject = customer_subject.get().strip()
        date = customer_date.get()
        info = customer_info.get("1.0", 'end-1c')

        if not selected_customer_name or not subject:
            messagebox.showerror("Input Error", "Please enter both a customer and subject.")
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            # Check if the customer and subject already exist
            cursor.execute(
                "SELECT name, subject FROM customer WHERE LOWER(name) = LOWER(?) AND LOWER(subject) = LOWER(?)",
                (selected_customer_name, subject))
            if cursor.fetchone():
                messagebox.showerror("Error", "Subject for this customer already exists!")
            else:
                # Insert new customer and subject
                cursor.execute("INSERT INTO customer (name, subject, date, info, modifydate) VALUES (?, ?, ?, ?, ?)",
                               (selected_customer_name, subject, date, info, current_date))
                conn.commit()
                messagebox.showinfo("Success", "Record added successfully")

                # Clear inputs
                customer_subject.delete(0, END)
                customer_date.delete(0, END)
                customer_info.delete('1.0', END)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

    submit_btn = Button(file_add_frame, text='Save', bg='green', font=('Helvetica', 10), command=submit)
    submit_btn.grid(row=5, column=2, pady=(10, 0), padx=7)


def hide_all_frame():
    for frame in [file_add_frame, edit_edit_frame, edit_delete_frame, password_frame, main_frame, show_frame, add_user_frame]:
        frame.pack_forget()  # Hide all frames before switching

def show():
    hide_all_frame()

    # Load the database path from settings file
    db_path = load_settings()
    if not db_path:
        messagebox.showerror("Error", "Database path not set. Please configure the database.")
        return

    # Function to load all distinct customer names from the database
    def load_customer_names():
        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()

        cur_sor.execute("SELECT DISTINCT name FROM customer")
        customer_names = cur_sor.fetchall()
        conn.close()

        # Flatten the list of customer names
        return [name[0] for name in customer_names]

    # Function to load all subjects for a selected customer
    def load_subjects(customer_name, search_term=''):
        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()

        if search_term:
            query = "SELECT DISTINCT subject FROM customer WHERE name LIKE ? AND subject LIKE ? COLLATE NOCASE"
            cur_sor.execute(query, ('%' + customer_name + '%', '%' + search_term + '%'))
        else:
            query = "SELECT DISTINCT subject FROM customer WHERE name LIKE ? COLLATE NOCASE"
            cur_sor.execute(query, ('%' + customer_name + '%',))

        subjects = cur_sor.fetchall()
        conn.close()

        # Flatten the list of subjects
        return [subject[0] for subject in subjects]

    # Load the customer names into the dropdown menu
    customer_names_list = load_customer_names()

    # If no customers are found, show a message and return
    if not customer_names_list:
        messagebox.showinfo("No Data", "No customers found in the database.")
        return

    # Create the frame for showing records
    global show_frame
    show_frame = customtkinter.CTkFrame(master=root, width=800, height=600, fg_color='gray')
    show_frame.pack(pady=20, padx=60, fill='both', expand=True)
    show_frame.grid_columnconfigure(1, weight=1)  # The second column (index 1) has more weight
    # Customer Name Dropdown Menu
    customer_name_var = StringVar(show_frame)
    customer_name_var.set(customer_names_list[0])  # Set the first customer as default

    name_lbl = CTkLabel(show_frame, text='Customer Name:', font=('Helvetica', 15), justify=LEFT)
    name_lbl.grid(row=0, column=0, pady=(10, 0), padx=7, sticky='e')

    customer_dropdown = customtkinter.CTkOptionMenu(show_frame, width=250, values=customer_names_list, variable=customer_name_var)
    customer_dropdown.grid(row=0, column=1, padx=(10, 0), pady=5, sticky="nsew")

    # Subject Search Box
    search_var = StringVar(show_frame)

    # Subject Dropdown Menu (Initially empty until customer is selected)
    subject_var = StringVar(show_frame)

    sub_lbl = CTkLabel(show_frame, text='Subject:', font=('Helvetica', 15), justify=LEFT)
    sub_lbl.grid(row=1, column=0, pady=(10, 0), padx=7, sticky='e')

    subject_dropdown = customtkinter.CTkOptionMenu(show_frame, width=250, values=[], variable=subject_var)
    subject_dropdown.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="nsew")

    search_lbl = CTkLabel(show_frame, text='Search Subject:', font=('Helvetica', 15), justify=LEFT)
    search_lbl.grid(row=2, column=0, pady=(10, 0), padx=7, sticky='e')
    search_box = CTkEntry(show_frame, textvariable=search_var, width=250)
    search_box.grid(row=2, column=1, padx=(10, 0), pady=5, sticky="nsew")

    # Function to update the subjects dropdown based on selected customer and search term
    def update_subjects_dropdown(selected_customer_name, search_term=''):
        subjects_list = load_subjects(selected_customer_name, search_term)
        if subjects_list:
            subject_var.set(subjects_list[0])  # Set the first subject as default
            subject_dropdown.configure(values=subjects_list)
        else:
            subject_var.set('')  # Clear the dropdown if no subjects are found
            subject_dropdown.configure(values=[])

    # Update subjects when customer is selected or search term is entered
    customer_dropdown.configure(command=lambda value: update_subjects_dropdown(value, search_var.get()))

    # Bind the search box to update subjects when typing
    search_box.bind('<KeyRelease>', lambda event: update_subjects_dropdown(customer_name_var.get(), search_var.get()))

    # Load subjects for the default customer on window load
    update_subjects_dropdown(customer_name_var.get())

    # Entry for Date and Info
    date_lbl = CTkLabel(show_frame, text='Date:', font=('Helvetica', 15), justify=LEFT)
    date_lbl.grid(row=3, column=0, pady=(10, 0), padx=7, sticky='e')
    date = CTkEntry(show_frame, width=250)
    date.grid(row=3, column=1, padx=(10, 0), pady=5, sticky="nsew")

    info_lbl = CTkLabel(show_frame, text='Info:', font=('Helvetica', 15))
    info_lbl.grid(row=4, column=0, pady=(10, 0), padx=7, sticky='ne')
    info = CTkTextbox(show_frame, height=450, width=400)
    info.grid(row=4, column=1, padx=(10, 0), pady=5, sticky="nsew")

    # Function to display the selected record's information
    def display_record(record):
        """ Display the customer data in the entry fields """
        date.delete(0, END)
        date.insert(0, record[4])
        info.delete('1.0', END)
        info.insert('1.0', record[3])

    # Function to fetch and display the first matching record for the selected customer and subject
    def fetch_record():
        customer_name = customer_name_var.get()
        subject = subject_var.get()

        if not customer_name or not subject:
            messagebox.showwarning("Input Error", "Please select both customer name and subject.")
            return

        conn = sqlite3.connect(db_path)
        cur_sor = conn.cursor()

        cur_sor.execute("SELECT * FROM customer WHERE name LIKE ? AND subject LIKE ? COLLATE NOCASE",
                        ('%' + customer_name + '%', '%' + subject + '%'))
        records = cur_sor.fetchall()

        if not records:
            messagebox.showinfo("No Records", "No matching records found.")
            conn.close()
            return

        global current_record_index
        current_record_index = 0
        total_records = len(records)

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

        # Display the first record
        display_record(records[current_record_index])

        # Create navigation buttons for the records
        button_frame = Frame(show_frame, bg='gray')
        button_frame.grid(row=5, column=0, columnspan=2, pady=(20, 0))

        prev_btn = CTkButton(button_frame, text='Previous', command=prev_record)
        next_btn = CTkButton(button_frame, text='Next', command=next_record)

        prev_btn.pack(side=LEFT, padx=20)
        next_btn.pack(side=RIGHT, padx=20)

        status_label = CTkLabel(show_frame, text=f"Record {current_record_index + 1} of {total_records}")
        status_label.grid(row=6, column=0, columnspan=2, pady=(20, 10))

        conn.close()

    # Fetch button to load the record when customer and subject are selected
    fetch_button = CTkButton(show_frame, text="Show Record", command=fetch_record)
    #fetch_button.grid(row=2, column=2, padx=10, pady=10)
    fetch_button.grid(row=2, column=2, padx=10, pady=5)



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

def add_user_window():
    hide_all_frame()
    add_user_frame.pack(pady=20, padx=60, fill='both', expand=True)
    """ Function to open a new window for adding users (admin only) """
    #user_window = Toplevel(root)
    #user_window.title("Add New User")
    #user_window.geometry(CenterDisplay(add_user_frame, 400, 300))

    # Labels and Entries for Username and Password
    Label(add_user_frame, text="New Username:").pack(pady=10)
    new_username_entry = customtkinter.CTkEntry(add_user_frame, width=250)
    new_username_entry.pack(pady=5)

    Label(add_user_frame, text="New Password:").pack(pady=10)
    new_password_entry = customtkinter.CTkEntry(add_user_frame, width=250, show='*')
    new_password_entry.pack(pady=5)

    def add_user():
        new_username = new_username_entry.get().strip()
        new_password = new_password_entry.get().strip()

        if not new_username or not new_password:
            messagebox.showerror("Input Error", "Username and Password cannot be empty.")
            return

        # Hash the password
        hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())

        # Insert the new user into the database
        db_path = load_settings()
        if not db_path:
            messagebox.showerror("Error", "Database path not set.")
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (new_username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
            conn.close()
            return

        # Insert new user
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, hashed_password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"User '{new_username}' added successfully!")
        add_user_frame.destroy()

    # Add Button
    add_button = Button(add_user_frame, text="Add User", command=add_user)
    add_button.pack(pady=20)

    #user_menu.add_command(label="Add User", command=add_user_window)

admin_user = "admin"  # Define the admin username
def delete_user_window():
    hide_all_frame()
    """ Function to open a new window for deleting users (admin only) """
    delete_user_win = Toplevel(root)
    delete_user_win.title("Delete User")
    delete_user_win.geometry(CenterDisplay(delete_user_win, 400, 300))

    # Labels and Listbox to show all users
    Label(delete_user_win, text="Select a User to Delete:").pack(pady=10)

    users_listbox = Listbox(delete_user_win, width=40, height=10)
    users_listbox.pack(pady=10)

    db_path = load_settings()
    if not db_path:
        messagebox.showerror("Error", "Database path not set.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all users from the database except for the admin
    cursor.execute("SELECT username FROM users WHERE username != ?", (admin_user,))
    users = cursor.fetchall()

    # Insert all users into the listbox
    for user in users:
        users_listbox.insert(END, user[0])

    conn.close()

    def delete_selected_user():
        selected_user = users_listbox.get(ACTIVE)

        if not selected_user:
            messagebox.showerror("Selection Error", "Please select a user to delete.")
            return

        confirm = messagebox.askyesno("Delete Confirmation", f"Are you sure you want to delete user '{selected_user}'?")
        if confirm:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Delete the selected user
            cursor.execute("DELETE FROM users WHERE username = ?", (selected_user,))
            conn.commit()
            conn.close()

            # Refresh the listbox after deletion
            users_listbox.delete(ACTIVE)
            messagebox.showinfo("Success", f"User '{selected_user}' has been deleted successfully.")

    # Delete Button
    delete_button = Button(delete_user_win, text="Delete User", command=delete_selected_user)
    delete_button.pack(pady=10)

def edit_user_window():
    hide_all_frame()
    add_user_frame.pack(pady=20, padx=60, fill='both', expand=True)

    Label(edit_user_frame, text="Select a User to Edit:").pack(pady=10)

    users_listbox = Listbox(edit_user_frame, width=40, height=10)
    users_listbox.pack(pady=10)

    db_path = load_settings()
    if not db_path:
        messagebox.showerror("Error", "Database path not set.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all users from the database except for the admin
    cursor.execute("SELECT username FROM users WHERE username != ?", (admin_user,))
    users = cursor.fetchall()

    # Insert all users into the listbox
    for user in users:
        users_listbox.insert(END, user[0])

    conn.close()

    # Function to load selected user details
    def load_selected_user():
        selected_user = users_listbox.get(ACTIVE)
        if not selected_user:
            messagebox.showerror("Selection Error", "Please select a user to edit.")
            return

        # Fetch the selected user's information from the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username = ?", (selected_user,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            username_entry.delete(0, END)
            username_entry.insert(0, user_data[0])
            password_entry.delete(0, END)  # Leave password empty for security reasons

    # Labels and input fields for editing the user
    Label(edit_user_frame, text="Username:").pack(pady=10)
    username_entry = customtkinter.CTkEntry(edit_user_frame, width=250)
    username_entry.pack(pady=5)

    Label(edit_user_frame, text="New Password (optional):").pack(pady=10)
    password_entry = customtkinter.CTkEntry(edit_user_frame, width=250, show='*')
    password_entry.pack(pady=5)

    def save_user_changes():
        selected_user = users_listbox.get(ACTIVE)
        new_username = username_entry.get().strip()
        new_password = password_entry.get().strip()

        if not selected_user or not new_username:
            messagebox.showerror("Input Error", "Username cannot be empty.")
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Check if the new username already exists (but is not the current user)
        cursor.execute("SELECT username FROM users WHERE username = ? AND username != ?", (new_username, selected_user))
        if cursor.fetchone():
            messagebox.showerror("Input Error", "Username already exists. Please choose another.")
            conn.close()
            return

        # Update the username (and password if provided)
        if new_password:
            hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
            cursor.execute("UPDATE users SET username = ?, password = ? WHERE username = ?", (new_username, hashed_password, selected_user))
        else:
            cursor.execute("UPDATE users SET username = ? WHERE username = ?", (new_username, selected_user))

        conn.commit()
        conn.close()

        # Update the listbox with the new username
        users_listbox.delete(ACTIVE)
        users_listbox.insert(END, new_username)
        messagebox.showinfo("Success", f"User '{selected_user}' has been updated to '{new_username}'")

    # Button to load the selected user's data
    load_button = Button(edit_user_frame, text="Load User", command=load_selected_user)
    load_button.pack(pady=10)

    # Button to save changes
    save_button = Button(edit_user_frame, text="Save Changes", command=save_user_changes)
    save_button.pack(pady=10)


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


# Menu for user management (only accessible by admin)
user_menu = Menu(my_menu)

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
add_user_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')
edit_user_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')
delete_user_frame = customtkinter.CTkFrame(master=root, width=800,height=600,fg_color='gray')



btn_query = CTkButton(root, text='Show records', command=show)
btn_query.pack(pady=20)
#btn_query = Button(root, text='Search-edit records', command=edit)
#btn_query.pack(pady=10)

search_btn = CTkButton(root, text="Edit Customer", command=search_window)
search_btn.pack(pady=20)
#lbl = customtkinter.CTkLabel(root, text='©arbtech')
#lbl.pack(anchor='se')

root.mainloop()