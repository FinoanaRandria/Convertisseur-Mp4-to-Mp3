from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import moviepy.editor as mp
from click import command
#follow Finoana Randria on Git hub
root = Tk()

root.title("Convertisseur Mp4 to Mp3 By Finoana Randri")
root.config(background="Orange")
root.iconbitmap("yad.ico")
root.geometry("500x500")

def mp4():
    thefile = filedialog.askopenfilename(initialdir="/",title="chosose video",filetypes=(("mp4 files","*.mp4"), ("wav files","*.wav")))
    clip = mp.VideoFileClip(thefile)
    clip.audio.write_audiofile(thefile+".mp3")

selectfile = Button(root,text="select file",command=mp4).pack(expand=YES)

root.mainloop()