from tkinter import *

import tkinter as tk
from tkinter import filedialog
import customtkinter
from customtkinter import CTk

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')
'''
def compare_files():
    file1_path = entry_file1.get()
    file2_path = entry_file2.get()
    output_path = entry_output.get()

    if not file1_path or not file2_path or not output_path:
        result_label.configure(text="Please provide file paths for both files and an output file.",text_color='red')
        return

    try:
        """
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines_file1 = set(file1.readlines())
            lines_file2 = set(file2.readlines())
            """
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines_file1 = file1.readlines()
            lines_file2 = file2.readlines()

            # missing_lines = lines_file1.difference(lines_file2)
            missing_lines = [line for line in lines_file1 if line not in lines_file2]

            with open(output_path, 'w') as output_file:
                output_file.writelines(missing_lines)

            result_label.configure(text="Comparison completed. Missing lines saved to the output file.",text_color='green')
    except Exception as e:
        result_label.configure(text=f"An error occurred: {str(e)}")
'''
def compare_files():
    file1_path = entry_file1.get()
    file2_path = entry_file2.get()
    output_path = entry_output.get()

    if not file1_path or not file2_path or not output_path:
        result_label.configure(text="Please provide file paths for both files and an output file.", text_color='red')
        return

    try:
        # Read files in binary mode to bypass encoding issues
        with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
            # Read binary content and decode using safe method (ignores errors)
            lines_file1 = [line.decode('utf-8', errors='ignore').strip() for line in file1.readlines()]
            lines_file2 = [line.decode('utf-8', errors='ignore').strip() for line in file2.readlines()]

        # Find missing lines from file1 (lines present in file1 but not in file2)
        missing_lines_file1 = [line for line in lines_file1 if line not in lines_file2]

        # Write only missing lines from file1 to the output file, preserving the original order of file1
        with open(output_path, 'w') as output_file:
            for line in missing_lines_file1:
                output_file.write(line + '\n')

        if missing_lines_file1:
            result_label.configure(text="Comparison completed. Missing lines from file1 saved to the output file.", text_color='green')
        else:
            result_label.configure(text="No missing lines found in file1.", text_color='green')

    except Exception as e:
        result_label.configure(text=f"An error occurred: {str(e)}", text_color='red')


def browse_file1():
    file1_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.*")])
    entry_file1.delete(0, "end")
    entry_file1.insert(0, file1_path)

def browse_file2():
    file2_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.*")])
    entry_file2.delete(0, "end")
    entry_file2.insert(0, file2_path)

def browse_output():
    output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    entry_output.delete(0, "end")
    entry_output.insert(0, output_path)

# Window center display function
def CenterDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width / 2) - (width / 2)) * scale_factor)
    y = int(((screen_height / 2) - (height / 1.9)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

# Create the main application window
root = customtkinter.CTk()

root.geometry(CenterDisplay(root,600, 250 ))
#Place the window on the center
#root.eval('tk::PlaceWindow . center')
#Title of the application
root.title("File Comparison Tool")
#Creating a frame
frame = LabelFrame(master=root,text='Text File Comparer',background='#ADD8E6')
#Creating a frame with border
#frame = LabelFrame(master=root,text='Text File Comparer',background='#ADD8E6',highlightbackground='blue',highlightthickness=2)
frame.pack(pady=20, padx= 50, fill='both', expand=True)
frame.grid_columnconfigure(1, weight=1) # to expand text box by dragging window

# Entry fields with placeholder
entry_file1 = customtkinter.CTkEntry(master=frame, placeholder_text='Select the new file:',width=150)
entry_file2 = customtkinter.CTkEntry(master=frame, placeholder_text='Select the old file:',width=150)
entry_output = customtkinter.CTkEntry(master=frame, placeholder_text='Save missing lines to:',width=150)

entry_file1.grid(row=0, column=1, padx = 10, pady=5,sticky="nsew")
entry_file2.grid(row=1, column=1, padx = 10, pady=5,sticky="nsew")
entry_output.grid(row=2, column=1, padx = 10, pady=5,sticky="nsew")

# Browse buttons
browse_button1 = customtkinter.CTkButton(master=frame, text="Browse", command=browse_file1)
browse_button2 = customtkinter.CTkButton(master=frame, text="Browse", command=browse_file2)
browse_button_output = customtkinter.CTkButton(master=frame, text="Browse", command=browse_output)

browse_button1.grid(row=0, column=2)
browse_button2.grid(row=1, column=2)
browse_button_output.grid(row=2, column=2)

# Compare button
compare_button = customtkinter.CTkButton(master=frame, text="Compare Files", command=compare_files)
compare_button.grid(row=3, column=2)

# Result label
result_label = customtkinter.CTkLabel(master=frame, text="", wraplength=300)
result_label.grid(row=4, column=0, columnspan=3)
lbl = Label(root, text='©arbtech')
lbl.pack(anchor='se')
# Start the Tkinter event loop
root.mainloop()
