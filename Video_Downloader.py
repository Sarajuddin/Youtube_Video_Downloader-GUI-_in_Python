from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import pytube
import platform
import time
import csv
import os
import socket
import tkinter.messagebox


win = Tk()
win.geometry("480x650")
win.title("Downloader")
win.resizable(0,0)

def information():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    version = platform.platform()
    type = platform.architecture()
    t = time.ctime()
    url=e1.get()
    data = (t, hostname, ip_address, version, type, url)
    if os.path.exists("data.csv"):
        with open('data.csv', mode = 'a', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(data)
    else:
        with open('data.csv', mode = 'w', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(data)

def download():
    information()
    url = e1.get()
    con = pytube.YouTube(url)
    lst = []
    try:
        streams = con.streams
        my_formats = {'itag="139"':"48kbps", 'itag="140"':"128kbps", 'itag="251"':"160kbps", 'itag="394"':"144p", 'itag="133"':"240p", 'itag="18"':"360p", 'itag="397"':"480p", 'itag="22"':"720p", 'itag="137"':"1080p", 'itag="400"':"1440p"}
        for itag in my_formats:
            for stream in streams:
                if itag in str(stream):
                    print(my_formats[itag])
                    lst.append(my_formats[itag])
    except:
        tkinter.messagebox.askokcancel("Warning", "Please check your Internet Conection or URL.\nIt looks like you are not connected to the internet.")
    
    def getFormat():
        user_format = combo.get()
        print(user_format)
        for key in my_formats:
            if my_formats[key]==user_format:
                new_itag = key
                # print(f"User selected {user_format} and its corresponding itag is : {new_itag}")
                return new_itag
    def startDownload():
        new_itag = getFormat()
        for stream in streams:
            if new_itag in str(stream):
                # print(f"Stream is found i.e. \n{stream}")
                break
        # print('Downloading starts...')
        stream.download("E:/Youtube Videos")
        label3 = Label(frm, text="Downloading starts...")
        label3.place(x=50, y=300)

    frm = Frame()
    frm.place(x=0, y=0, width=480, height=650)  
    label1 = Label(frm, text="Connection is being established. Please Wait...", font=('arial', 12))
    label1.place(x=80, y=50)
    
    label2 = Label(frm, text="Select any format:", font=('arial', 14, 'bold'))
    label2.place(x=80, y=130)
    combo = Combobox(frm, font=("Arial", 14), values=lst)
    combo.place(x=80, y=170, width=280, height=30)
    btn1 = Button(win, text="Next >>", font=('arial', 16, 'bold'), fg="white", bg="darkred", command=startDownload)
    btn1.place(x=80, y=225)
    # --------------------------------------
    label3 = Label(frm, text="--- Made By ~ Sarajuddin ---", font=("Arial", 12, "bold"), fg="white", bg="darkred")
    label3.pack(side=BOTTOM, fill=X)         

def validatelink():
    link = e1.get()
    if not link:
        tkinter.messagebox.askokcancel("Warning", "Please enter valid link.")
    else:
        download()

img = Image.open("./logo.png")
img = img.resize((150,100))
imgtk = ImageTk.PhotoImage(img, master=win)
img_label = Label(win, image=imgtk)
img_label.place(x=30, y=50)

label1 = Label(win, text="Video Downloader", font=('arial', 20, 'bold'), fg="darkred")
label1.place(x=150, y=85)
entry_label1 = Label(win, text="Enter the link:", font=('arial', 14))
entry_label1.place(x=80, y=250)
e1= Entry(win, font=('arial', 12), width=35)
e1.place(x=80, y=285)

btn1 = Button(win, text="Next >>", font=('arial', 16, 'bold'), fg="white", bg="darkred", command=validatelink)
btn1.place(x=80, y=325)
label2 = Label(win, text="--- Made By ~ Sarajuddin ---", font=("Arial", 12, "bold"), fg="white", bg="darkred")
label2.pack(side=BOTTOM, fill=X)


if __name__ == '__main__':
    win.mainloop()