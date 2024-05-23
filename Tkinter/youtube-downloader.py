import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Function to download the video
def download_video():
    try:
        url = entry.get()
        yt = YouTube(url)
        #stream = yt.streams.get_highest_resolution()
        stream = yt.streams.get_audio_only()
        stream.download()
        messagebox.showinfo("Success", "Download complete.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("YouTube Downloader")

# Create a label
label = tk.Label(root, text="Enter the YouTube URL:")
label.pack()

# Create an entry field to input the URL
entry = tk.Entry(root, width=40)
entry.pack()

# Create a download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Start the Tkinter event loop
root.mainloop()
