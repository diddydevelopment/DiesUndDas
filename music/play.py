import vlc
import tkinter

p = vlc.MediaPlayer('house1.mp3')

p.play()


root = tkinter.Tk()

label = tkinter.Label(root,text='Mein Musicplayer')

label.pack()

root.mainloop()