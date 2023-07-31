from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()

root.title('Translator')
root.config(bg='#31906E')
root.geometry('835x300')
root.resizable(0,0)

def translate():

    translated_text.delete(1.0, END)
    try:
        # Get the languages from dictionary keys
        # Get the from language key
        for key, value in languages.items():
            if (value == source_combo.get()):
                from_language_key = key
        # Get the to language key
        for key, value in languages.items():
            if (value == dest_combo.get()):
                to_language_key = key

        # Turn original text into a textblob
        words = textblob.TextBlob(translate_text.get(1.0, END))

        # Translate text
        words = words.translate(from_lang=from_language_key, to = to_language_key)

        # Out put translated text to screen
        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror('Translator', e)


def clear():
    translate_text.delete(1.0, END)
    translated_text.delete(1.0, END)

def copy():
    # Clear the clipborad
    root.clipboard_clear()
    # Copy to clipborad
    root.clipboard_append(translated_text.get(1.0, END))

# Grab Lanbguage list from GoogleTrans

languages = googletrans.LANGUAGES
# Convert to list
language_list = list(languages.values())


translate_text = Text(root, height=10, width=40)
translate_text.grid(row=0, column=0, pady=15, padx=10)

trans_button = Button(root, text='Translate', font=('Helvetica', 20), bg='#5865F2',fg='white', command=translate)
trans_button.grid(row=0, column=1, pady=5, padx=5)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=15, padx=10)

copyButton = Button(root,text='Copy', font=('Helvetica', 10),bg='#5865F2',fg='white', command=copy)
copyButton.grid(row=1,column=2, padx=(290,10))

source_combo = ttk.Combobox(root, width=50, value = language_list)
source_combo.current(21)
source_combo.grid(row=2, column=0)

clear_button = Button(root, text='Clear', font=('Helvetica', 20),bg='#5865F2',fg='white', command=clear)
clear_button.grid(row=2, column=1)

dest_combo = ttk.Combobox(root, width=50, value = language_list)
dest_combo.current(25)
dest_combo.grid(row=2, column=2)

lb = Label(root,text='©arb', bg='#31906E')
lb.grid(row=3,column=2, padx=(290,2), pady=2)

root.mainloop()
