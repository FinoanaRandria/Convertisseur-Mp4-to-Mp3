from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from turtle import bgcolor, left, width
import moviepy.editor as mp
from click import command
#follow Finoana Randria on Git hub
root = Tk()
 #variable

root.title("Convertisseur Mp4 to Mp3 By Finoana Randri")
root.config(background="#12EBCE")
#root.iconbitmap("yad.ico")
root.geometry("500x500")
root.minsize(500,500)
#mon image
width =400
heigth =400
image = PhotoImage(file="k.png").zoom(30).subsample(30)
canvas = Canvas(root,width=width,height=heigth,bg="#12EBCE",bd=0,highlightthickness=0)
canvas.create_image(width/2,heigth/2,image=image)
canvas.pack(expand=YES)

def mp4():
    thefile = filedialog.askopenfilename(initialdir="/",title="chosose video",filetypes=(("mp4 files","*.mp4"), ("wav files","*.wav")))
    clip = mp.VideoFileClip(thefile)
    clip.audio.write_audiofile(thefile+".mp3")
gradient = PhotoImage(file='index.png')
selectfile = Button(root,image=gradient,bg="#12EBCE",border=0,command=mp4).pack(expand=YES)


#barre de menu

menu_bar = Menu(root,bg="white")

#preminer menu(i love python now but i am beginer  XD FinoanaRandria)
file_menu = Menu(menu_bar ,tearoff=0)
file_menu.add_command(label="Quit" ,command=root.quit)
menu_bar.add_cascade(label="Options",menu=file_menu)

#insertion dans la fenetre
root.config(menu=menu_bar)
root.mainloop()