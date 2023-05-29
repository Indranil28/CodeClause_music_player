import tkinter as tk
import fnmatch
import os
from pygame import mixer

mixer.init()

canvas=tk.Tk()
canvas.title("music player ")
canvas.geometry("600x800")
canvas.config(bg="black")

rootpath="C:\\Users\KIIT\Downloads\music"
pattern="*.mp3"


def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select.clear('active')

def play_next():
    next_song=listbox.curselection()
    next_song=next_song[0]+1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath+"\\"+listbox.get("anchor"))
    mixer.music.play()
    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    next_song=listbox.curselection()
    next_song=next_song[0]-1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath+"\\"+listbox.get("anchor"))
    mixer.music.play()
    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def pause_song():
    if pausebutton["text"]=="pause":
        mixer.music.pause()
        pausebutton["text"]="play"
    else:
        mixer.music.unpause()
        pausebutton["text"]="pause"

listbox=tk.Listbox(canvas,fg="green",bg="black",width=100,font=('poppins',14))
listbox.pack(padx=15 , pady=15)

label=tk.Label(canvas,text='',fg="yellow",bg="black",width=100,font=('poppins',14))
label.pack(pady=15)

top=tk.Frame(canvas,bg='black')
top.pack(padx=10,pady=5,anchor='center')


prevbutton=tk.Button(canvas,text='prev',command=play_prev)
prevbutton.pack(pady=15,in_=top,side='left')

stopbutton=tk.Button(canvas,text='stop',command=stop)
stopbutton.pack(pady=15,in_=top,side='left')

pausebutton=tk.Button(canvas,text='pause',command=pause_song)
pausebutton.pack(pady=15,in_=top,side='left')

startbutton=tk.Button(canvas,text='start',command=select)
startbutton.pack(pady=15,in_=top,side='left')

nextbutton=tk.Button(canvas,text='next',command=play_next)
nextbutton.pack(pady=15,in_=top,side='left')

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert('end',filename)


canvas.mainloop()