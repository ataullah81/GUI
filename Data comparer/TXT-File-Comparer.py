
import tkinter as tk
from tkinter import filedialog


def compare_files():
    file1_path = entry_file1.get()
    file2_path = entry_file2.get()
    output_path = entry_output.get()

    if not file1_path or not file2_path or not output_path:
        result_label.config(text="Please provide file paths for both files and an output file.")
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

            result_label.config(text="Comparison completed. Missing lines saved to the output file.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}")

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

# Create the main application window
root = tk.Tk()
root.geometry('320x150')

root.title("File Comparison Tool")


# Labels
label_file1 = tk.Label(root, text="Select the first text file:")
label_file2 = tk.Label(root, text="Select the second text file:")
label_output = tk.Label(root, text="Save missing lines to:")

label_file1.grid(row=0, column=0)
label_file2.grid(row=1, column=0)
label_output.grid(row=2, column=0)

# Entry fields
entry_file1 = tk.Entry(root)
entry_file2 = tk.Entry(root)
entry_output = tk.Entry(root)

entry_file1.grid(row=0, column=1)
entry_file2.grid(row=1, column=1)
entry_output.grid(row=2, column=1)

# Browse buttons
browse_button1 = tk.Button(root, text="Browse", command=browse_file1)
browse_button2 = tk.Button(root, text="Browse", command=browse_file2)
browse_button_output = tk.Button(root, text="Browse", command=browse_output)

browse_button1.grid(row=0, column=2)
browse_button2.grid(row=1, column=2)
browse_button_output.grid(row=2, column=2)

# Compare button
compare_button = tk.Button(root, text="Compare Files", command=compare_files)
compare_button.grid(row=3, column=1)

# Result label
result_label = tk.Label(root, text="", wraplength=300)
result_label.grid(row=4, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()
