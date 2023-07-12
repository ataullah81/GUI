import tkinter as tk
import time
import datetime as dt
from playsound import playsound

root = tk.Tk()
root.geometry("500x300")
root.title("Alarm Clock")


def set_alarm():
    alarm_time = entry.get() # get the user input from Entry widget
    try:
        alarm_time = dt.datetime.strptime(alarm_time, '%H:%M:%S')
    except ValueError:
        status_label.config(text="Invalid time format")
        return
    status_label.config(text=f"Alarm set for {alarm_time}")
    #check_alarm(alarm_time)
    while True:
        time.sleep(1) # wait for 1 second
        current_time = time.strftime("%H:%M:%S") # get the current time
        if current_time == alarm_time:
            message = tk.Label(root, text="Time's up!", font=("Arial", 16))
            message.pack()
            playsound('alarm.mp3') # play the alarm sound
            break

def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry.get() == 'Enter time in 24 hour format (HH:MM:SS)':
        entry.delete(0, tk.END) # delete all the text in the entry
        entry.insert(0, '') #Insert blank for user input

def on_focusout(event):
    """function that gets called whenever entry focus is lost"""
    if entry.get() == '':
        entry.insert(0, 'Enter time in 24 hour format (HH:MM:SS)')

def update_time():
    """Update the current time label"""
    now = dt.datetime.now()
    time_label.config(text=now.strftime('%H:%M:%S'))
    root.after(1000, update_time)

# Create a label to display the alarm status
status_label = tk.Label(root, font=('calibri', 20))
status_label.pack(pady=10)

# Create a label for the current time
time_label = tk.Label(root, font=('calibri', 40))
time_label.pack(pady=20)

entry = tk.Entry(root, width=30, font=('Arial', 14), fg='grey')
entry.insert(0, 'Enter time in 24 hour format (HH:MM:SS)')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(pady=20)

button = tk.Button(root, text="Set Alarm", font=("Arial", 12), command=set_alarm)
button.pack()

# Start the clock
update_time()

root.mainloop()
