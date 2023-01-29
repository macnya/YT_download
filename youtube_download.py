from tkinter import *
from pytube import YouTube

def download_video():
    video_url = entry.get()
    yt = YouTube(video_url)
    video = yt.streams.first()
    video.download()
    label.config(text="Download Complete!")

root = Tk()
root.title("YouTube Video Downloader")

label = Label(root, text="Enter video URL:")
label.pack()

entry = Entry(root)
entry.pack()

download_button = Button(root, text="Download Video", command=download_video)
download_button.pack()

root.mainloop()

