import tkinter as tk
import ssl
from pytube import YouTube
import os

ssl._create_default_https_context = ssl._create_stdlib_context
invalidStr = '<>:"/\|?*'


def buttonGet():
    url = var_url.get()
    label3 = tk.Label(window, text="")
    name = var_filename.get()
    if url == "" or url == " ":
        label3.place(x=140, y=140)
        label3.config(font=("微軟正黑體", 20), text="請輸入影片網址!", foreground="red")
    else:
        label3.place(x=140, y=140)
        label3.config(
            text="                                     ",
            font=("微軟正黑體", 20),
            foreground="red",
        )
        # print("destory")
        entry.delete(0, "end")
        res = DownloadMP3(url, name)
        if not res:
            label3.config(
                font=("微軟正黑體", 20),
                text="網址輸入錯誤!         ",
                foreground="red",
            )
        else:
            label3.config(
                font=("微軟正黑體", 20),
                text="下載成功!             ",
                foreground="green",
            )


def DownloadMP3(url, name):
    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    try:
        yt = YouTube(url)
        if name == "" or name == None:
            title = yt.title
            try:
                for i in invalidStr:
                    if i in title:
                        title = title.replace(i, "")
                yt.streams.filter().get_audio_only().download(
                    output_path=desktop, filename=title + ".mp3"
                )
                return 1
            except Exception as e:
                print(e)
                return 0
        else:
            for i in invalidStr:
                if i in name:
                    name = name.replace(i, "")
                else:
                    yt.streams.filter().get_audio_only().download(
                        filename=name + ".mp3"
                    )
        return 1
    except Exception as e:
        print(e)
        return 0


window = tk.Tk()
window.title("YoutubeMP3下載器")
window.geometry("500x200")
window.resizable(False, False)
window.iconbitmap("soda7592.ico")
var_url = tk.StringVar()
var_filename = tk.StringVar()

label = tk.Label(window, text="影片網址: ")
label.grid(pady=10, row=0, column=0)
label.config(font=("微軟正黑體", 24))
entry = tk.Entry(window, textvariable=var_url)
entry.grid(ipady=5, row=0, column=1)

label2 = tk.Label(window, text="檔案名稱: ")
label2.grid(pady=15, row=1, column=0)
label2.config(font=("微軟正黑體", 24))
entry2 = tk.Entry(window, textvariable=var_filename)
entry2.grid(ipady=5, row=1, column=1)

button = tk.Button(window, text="下載音檔", command=buttonGet)
button.config(font=("微軟正黑體", 20))
button.grid(padx=20, row=0, column=3)
window.mainloop()
