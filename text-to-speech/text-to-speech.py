from tkinter import *
import pyttsx3

root = Tk()
root.title('Text to Speech')
root.geometry('800x500')
root.config(bg='#00A36C')


def textToSpeech():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # # getting details of current speaking rate
    engine.setProperty('rate', 150)  # setting up new voice rate
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(entryBox.get())
    engine.runAndWait()


def clear_text():
    entryBox.delete(0, END)


lf = LabelFrame(root, text='Write your text', font=('Helvetica', 20), bg='#438D80', fg='white')
lf.pack(pady=30)

entryBox = Entry(lf, width=50, font=('Helvetica', 16))
entryBox.pack(pady=20, padx=20)

my_button = Button(root, text='Convert Text to Speech', font=('Helvetica', 20), relief='sunken', bg='#00A36C', fg='white', bd=5, activebackground='#00A36C', command=textToSpeech)
my_button.pack()

clear_button = Button(root, text='Clear Text', font=('Helvetica', 20), relief='sunken', bg='#00A36C', fg='white', bd=5, activebackground='#00A36C', command=clear_text)
clear_button.pack(pady=20)

lb = Label(root,text='©arb',bg='#00A36C')
lb.pack(anchor='se', pady=(150, 5), padx=5)

root.mainloop()
