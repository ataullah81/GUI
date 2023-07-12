from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from time import sleep
from pygame import mixer

# color
bg_color = 'white'
col = 'blue'
col2 = 'black'

# window
window = Tk()
window.title('Alarm Clock')
window.geometry('350x150')
window.configure(bg=bg_color)
head = Label(window, text='Alarm clock', font=('comic sans',20))
head.grid(row=0,columnspan=3)

window.title('Alarm Clock')
window.geometry('350x150')


def sound_alarm():
    mixer.music.load('alarm.mp3')
    mixer.music.play()

def alarm():
    while True:
        control = 1
        print(control)
        alarm_hour = '02'
        alarm_minute = '47'
        alarm_sec = '00'
        alarm_period = 'PM'.upper()

        now = datetime.now()

        hour = now.strftime('%I')
        minute = now.strftime('%M')
        second = now.strftime('%S')
        period = now.strftime('%p')

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print('Time to take a break')
                            sound_alarm()
        sleep(1)

mixer.init()
alarm()
window.mainloop()