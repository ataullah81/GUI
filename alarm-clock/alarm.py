from tkinter.ttk import *
from tkinter import *

from pygame import mixer


# window
window = Tk()
window.title('Alarm Clock')
window.geometry('350x150')
window.mainloop()

def sound_alarm():
    mixer.music.load('')