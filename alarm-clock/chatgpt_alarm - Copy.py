import tkinter as tk
import datetime as dt
from tkinter import messagebox

from pygame import mixer
import time

mixer.init()


class AlarmClock:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Alarm Clock")

        # Create a label for the current time
        self.time_label = tk.Label(self.window, font=('calibri', 40))
        self.time_label.pack(pady=20)

        # Create an entry widget to get the alarm time
        self.alarm_entry = tk.Entry(self.window, font=('calibri', 20))
        self.alarm_entry.insert(0, "H:M:S")
        self.alarm_entry.pack(pady=10)

        #self.alarm_entry.bind('<FocusIn>', self.alarm_entry.delete(0, 'end'))

        # Create a button to set the alarm
        self.set_button = tk.Button(self.window, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)

        # Create a label to display the alarm status
        self.status_label = tk.Label(self.window, font=('calibri', 20))
        self.status_label.pack(pady=10)

        # Start the clock
        self.update_time()

        self.window.mainloop()

    def update_time(self):
        """Update the current time label"""
        now = dt.datetime.now()
        self.time_label.config(text=now.strftime('%H:%M:%S'))
        self.window.after(1000, self.update_time)

    def set_alarm(self):
        """Set the alarm"""
        alarm_time_str = self.alarm_entry.get()
        try:
            alarm_time = dt.datetime.strptime(alarm_time_str, '%H:%M:%S')
        except ValueError:
            self.status_label.config(text="Invalid time format")
            return

        self.status_label.config(text=f"Alarm set for {alarm_time_str}")
        self.check_alarm(alarm_time)

    def check_alarm(self, alarm_time):
        """Check if the current time matches the alarm time"""
        now = dt.datetime.now()
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute and now.second == alarm_time.second:
            self.status_label.config(text="Alarm ringing!")

            # Insert code to play an alarm sound here
            mixer.music.load('alarm.mp3')
            mixer.music.play(3)
            # self.status_label.config(text="Ok")
            msg = messagebox.showinfo('Stop Alarm')
            if msg == 'ok':
                mixer.music.stop()

        else:
            self.window.after(1000, self.check_alarm, alarm_time)


if __name__ == "__main__":
    alarm_clock = AlarmClock()
