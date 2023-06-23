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
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
def PlayMusic():
    Music = PlayList.get(ACTIVE)
    print(Music(ACTIVE))
    mixer.music.load(PlayList.get(ACTIVE))
    mixer.music.play()
 

frame = Frame(root, bg="#9E829C", width=485,height=180)
frame.place(x=0, y= 350)
logo_img = PhotoImage(file="logo.png")
root.iconphoto(False, logo_img)
Menu = PhotoImage(file = "menu.png")
Label(root,image=Menu).place(x=0, y=500,width=485,height=100)
frame_music = Frame(root, bd = 2, relief=RIDGE)
frame_music.place(x= 0, y=550, width = 485, height=100)
Button(root, text = "Browse Music", width = 60, height = 1, font=("ariel, 12, italic"), fg="Black", bg="Seashell", command=AddMusic).place(x=0, y = 500)
Scroll= Scrollbar(frame_music)
root.mainloop()