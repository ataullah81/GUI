import tkinter as tk
import customtkinter as ctk
from tkcalendar import Calendar
from datetime import datetime


def show_calendar():
    def select_date():
        selected_date = cal.get_date()
        date_entry.delete(0, tk.END)
        date_entry.insert(0, selected_date)
        top.destroy()

    top = tk.Toplevel(root)
    top.grab_set()
    cal = Calendar(top, selectmode='day', date_pattern='mm/dd/yyyy')
    cal.pack(pady=20)

    select_btn = ctk.CTkButton(top, text="Select", command=select_date)
    select_btn.pack(pady=10)


def get_selected_date():
    selected_date = date_entry.get()
    try:
        datetime.strptime(selected_date, '%m/%d/%Y')
        ctk.CTkMessageBox.show_info("Selected Date", f"You selected: {selected_date}")
    except ValueError:
        ctk.CTkMessageBox.show_error("Invalid Date", "The date format should be mm/dd/yyyy.")


# Create the main application window
root = ctk.CTk()
root.title("Dropdown Calendar")

# Create and place the date entry widget
ctk.CTkLabel(root, text="Select Date:").pack(pady=10)
date_entry = ctk.CTkEntry(root)
date_entry.pack(pady=10)

# Create and place the button to show the calendar
calendar_btn = ctk.CTkButton(root, text="Pick a Date", command=show_calendar)
calendar_btn.pack(pady=10)

# Create and place the button to get the selected date
submit_btn = ctk.CTkButton(root, text="Get Selected Date", command=get_selected_date)
submit_btn.pack(pady=10)

# Run the application
root.mainloop()
