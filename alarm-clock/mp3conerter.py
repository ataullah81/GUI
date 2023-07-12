import tkinter as tk
from tkinter import messagebox
import os
from pytube import YouTube
from pydub import AudioSegment
import ffmpeg

# Create tkinter window
window = tk.Tk()
window.title("YouTube to MP3 Converter")

# Define function to convert video
def convert_video():
    try:
        url = url_entry.get()
        if url != "":
            yt = YouTube(url)
            title = yt.title
            video_path = yt.streams.filter(only_audio=True).first().download()
            audio = AudioSegment.from_file(video_path)
            mp3_path = os.path.splitext(video_path)[0] + ".mp3"
            audio.export(mp3_path, format="mp3")
            os.remove(video_path)
            messagebox.showinfo("YouTube to MP3 Converter", f"{title} - Conversion Complete")
    except Exception as e:
        messagebox.showerror("YouTube to MP3 Converter", f"Error: {e}")

# Create label and entry for URL
url_label = tk.Label(window, text="Enter YouTube Video URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Create convert button
convert_button = tk.Button(window, text="Convert", command=convert_video)
convert_button.pack()

# Run tkinter window
window.mainloop()