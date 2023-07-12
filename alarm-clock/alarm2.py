from tkinter import *
import datetime
import time
from pygame import mixer
from tkinter import messagebox

# color
bg_color = 'Green'
col = 'gray'
col2 = 'black'

root = Tk()
root.title('Alarm Clock')
# root.geometry('530x330')
root.geometry('400x250')
root.configure(bg=bg_color)

alarm_time = StringVar()
msgi = StringVar()

head = Label(root, text='Alarm Clock', font=('comic sans', 20))
head.grid(row=0, columnspan=3, pady=10)

mixer.init()


def alarm():
    alarmT = alarm_time.get()

    current_time = time.strftime('%H:%M')

    while alarmT != current_time:
        current_time = time.strftime('%H:%M')
    if alarmT == current_time:
        mixer.music.load('alarm.mp3')
        mixer.music.play(3)
        msg = messagebox.showinfo('Info', f'{msgi.get()}')
        if msg == 'ok':
            mixer.music.stop()


clocking = PhotoImage(file='alarm-clock-80.png')
img = Label(root, image=clocking, bg=bg_color)
img.grid(rowspan=4, column=0)

input_time = Label(root, text='Input time', font=('comic sans', 15))
input_time.grid(row=1, column=1)

altime = Entry(root, textvariable=alarm_time, font=('comic sans', 18), width=6)
altime.grid(row=1, column=2)

msg = Label(root, text='Massage', font=('comic sans', 18))
msg.grid(row=2, column=1, columnspan=2)

msginput = Entry(root, textvariable=msgi, font=('comic sans', 18))
msginput.grid(row=3, column=1, columnspan=2)

submit = Button(root, text='SUBMIT', font=('comic sans', 18), bg=col, command=alarm)
submit.grid(row=4, column=1, columnspan=2)

root.mainloop()
