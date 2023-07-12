import datetime as dt
import os
import sys
import tkinter as tk
from tkinter import messagebox

from pygame import mixer

mixer.init()
root = tk.Tk()
root.geometry("500x300")
root.title("Alarm Clock")


def set_alarm():
    alarm_time_str = entry.get()  # get the user input from Entry widget
    try:
        alarm_time = dt.datetime.strptime(alarm_time_str, '%H:%M:%S')
    except ValueError:
        status_label.config(text="Invalid time format")
        return
    status_label.config(text=f"Alarm set for {alarm_time_str}")
    check_alarm(alarm_time)


def check_alarm(alarm_time):
    """Check if the current time matches the alarm time"""
    now = dt.datetime.now()
    if now.hour == alarm_time.hour and now.minute == alarm_time.minute and now.second == alarm_time.second:
        status_label.config(text="Alarm ringing!")

        # Insert code to play an alarm sound here
        ROOT_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

        mixer.music.load(os.path.join(ROOT_DIR, 'alarm.mp3'))
        # mixer.music.load('alarm.mp3')
        mixer.music.play(3)
        # self.status_label.config(text="Ok")
        msg = messagebox.showinfo('Stop Alarm', 'Alarm ringing')
        if msg == 'ok':
            mixer.music.stop()

    else:
        root.after(1000, check_alarm, alarm_time)


def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry.get() == '24 hour format (HH:MM:SS)':
        entry.delete(0, tk.END)  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input


def on_focusout(event):
    """function that gets called whenever entry focus is lost"""
    if entry.get() == '':
        entry.insert(0, '24 hour format (HH:MM:SS)')


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
entry.insert(0, '24 hour format (HH:MM:SS)')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(pady=20)

button = tk.Button(root, text="Set Alarm", font=("Arial", 12), command=set_alarm)
button.pack()

# Start the clock
update_time()

root.mainloop()
