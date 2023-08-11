import tkinter
import customtkinter
from pytube import YouTube


def startDownload(option):
    try:
        url = link.get()

        ytObject = YouTube(url, on_progress_callback=on_progress)
        if option == 'highQuality':
            video = ytObject.streams.get_highest_resolution()
        elif option == 'lowQuality':
            video = ytObject.streams.get_lowest_resolution()
        elif option == 'audio':
            video = ytObject.streams.get_audio_only()

        else:
            return

        title.configure(text=ytObject.title, text_color='white')
        finishLabel.configure(text='')
        video.download()
        finishLabel.configure(text='Downloaded', text_color='green')
    except:
        finishLabel.configure(text='Download error', text_color='red')
        raise

# Progress bar function

def on_progress(stream, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percentage_of_completion = bytes_download / total_size
    per = str(int(percentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()

    # Update progress bar
    progressbar.set(float(percentage_of_completion) / 100)


# System settings

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# App frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('Youtube Downloader')

# Adding UI elements

title = customtkinter.CTkLabel(app, text='Insert a youtube url:', width=200, height=50, font=('Helvetica', 20))
title.pack(pady=10, padx=10)

# Link input
url_var = tkinter.StringVar()

link = customtkinter.CTkEntry(app, width=500, height=50, textvariable=url_var)
link.pack(pady=10, padx=10)

# lbl_saveFile = customtkinter.CTkLabel(master=frame,text='Destination Directory').pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

# Progress percentage
progress = customtkinter.CTkLabel(app, text='0%')
progress.pack()

# ProgressBar
progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(pady=10, padx=10)

# Dowonload High quality viedo button
download_hq = customtkinter.CTkButton(app, text='Download High Quality-Mp4',
                                      command=lambda: startDownload('highQuality'))
download_hq.pack(pady=12, padx=10)

# Dowonload Low quality viedo button
download_lq = customtkinter.CTkButton(app, text='Download Low Quality-Mp4', command=lambda: startDownload('lowQuality'))
download_lq.pack(pady=12, padx=10)

# Dowonload Low quality viedo button
download_audio = customtkinter.CTkButton(app, text='Download Mp3', command=lambda: startDownload('audio'))
download_audio.pack(pady=12, padx=10)

# Run our app
app.mainloop()
