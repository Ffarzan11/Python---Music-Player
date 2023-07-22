import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("musify")
root.geometry("485x600+290+10")
root.configure(background="#3F334D")
root.resizable(False,False)
mixer.init()

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                PlayList.insert(END, song)
def PlayMusic():
    Music = PlayList.get(ACTIVE)
    print(Music(ACTIVE))
    mixer.music.load(PlayList.get(ACTIVE))
    mixer.music.play()
 

frame = Frame(root, bg="#9E829C", width=485,height=150)
frame.place(x=0, y= 300)
logo_img = PhotoImage(file="logo.png")
root.iconphoto(False, logo_img)
Menu = PhotoImage(file = "menu.png")
Label(root,image=Menu).place(x=0, y=450,width=485,height=100)
frame_music = Frame(root, bd = 2, relief=RIDGE)
frame_music.place(x= 0, y=450, width = 485, height=150)
ButtonPlay = PhotoImage(file="play.png")
Button(root, image = ButtonPlay, bg = "#FFFFFF", bd=0, height = 50, width = 50, command=PlayMusic).place(x=230,y=387)
ButtonStop = PhotoImage(file="stop.png")
Button(root, image = ButtonStop, bg = "#FFFFFF", bd=0, height = 50, width = 50, command=mixer.music.stop).place(x=170,y=387)
ButtonPause = PhotoImage(file="pause.png")
Button(root, image = ButtonPause, bg = "#FFFFFF", bd=0, height = 50, width = 50, command=mixer.music.pause).place(x=290,y=387)
Button(root, text = "Browse Music", width = 60, height = 1, font=("ariel", 12, "italic"), fg="Black", bg="Seashell", command=AddMusic).place(x=0, y = 450)
Scroll= Scrollbar(frame_music)
PlayList = Listbox(frame_music, width=100, font = ("ariel", 12),bg = "#3F334D", fg = "white", selectbackground="#9E829C", cursor="arrow", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=PlayList.yview)
Scroll.pack(side=RIGHT, fill= Y)
PlayList.pack(side=RIGHT, fill = BOTH)
root.mainloop()