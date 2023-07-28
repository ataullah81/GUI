from tkinter import *
import math
from pygame import mixer
import speech_recognition

mixer.init()

def click(value):
    # print(value)
    ex = entryField.get()
    answer = ''

    try:
        if value == 'C':
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):  # cube root
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':  # cube
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == 'rad':
            answer == math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(ex)

        elif value == chr(247):
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)


    except SyntaxError:
        pass
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a, b):
    l = math.lcm(a, b)
    return l

def hcf(a, b):
    h = math.gcd(a, b)
    return h

operations = {'ADD':add}
def audio():
    #print("Audio button clicked")
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m, duration=0.2)
            voice = sr.listen(m)
            text = sr.recognize_google(voice)
            print(text)
            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list = text.split(' ')
            print(text_list)
        except:
            pass




root = Tk()
root.title('Smart Calculator')
root.config(bg='lightgreen')
# root.geometry('680x486+100+100')
root.geometry('712x497+100+100')
root.resizable(0, 0)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage, bg='lightgreen')
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 20, 'bold'), bg='#2a2d36', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file='microphone.png')
micButton = Button(root, image=micImage, bd=0, bg='lightgreen', activebackground='lightgreen'
                   ,command=audio)
micButton.grid(row=0, column=7)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='#2a2d36', fg='white',
                    font=('arial', 18, 'bold'), activebackground='#2a2d36', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=2, padx=2)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
