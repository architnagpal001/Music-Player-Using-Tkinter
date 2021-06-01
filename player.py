from tkinter import *
import pygame
from PIL import Image,ImageTk
from tkinter import filedialog



root = Tk()
root.title("MP3 Player")
root.geometry("600x300")

# initialize pygame mixer
pygame.mixer.init()

# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='songs/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    song = song.replace("C:/Users/archi/OneDrive/Desktop/Tkinter/songs/", "")
    song = song.replace(".mp3", "")
    lbx.insert(END, song)

# Play Selected Song   
def play():
    song = lbx.get(ACTIVE)
    song = f'C:/Users/archi/OneDrive/Desktop/Tkinter/songs/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Stop playing Current Song
def stop():
    pygame.mixer.music.stop()
    lbx.selection_clear(ACTIVE)

#Create Playlist Box
lbx =Listbox(root, bg="black", fg="white", width=90, selectbackground="gray")
lbx.pack(pady=20)

# Define Player Control Buttons
back_btn = ImageTk.PhotoImage(file='images/back50.jpeg')
forward_btn = ImageTk.PhotoImage(file='images/forward50.jpeg')
play_btn = ImageTk.PhotoImage(file='images/play50.jpeg')
pause_btn = ImageTk.PhotoImage(file='images/pause50.jpeg')
stop_btn = ImageTk.PhotoImage(file='images/stop50.jpeg')

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
Button(controls_frame, image=back_btn, borderwidth=0).grid(row=0, column=0)
Button(controls_frame, image=forward_btn, borderwidth=0).grid(row=0, column=2)
Button(controls_frame, image=play_btn, borderwidth=0, command=play).grid(row=0, column=1)
Button(controls_frame, image=pause_btn, borderwidth=0).grid(row=0, column=3)
Button(controls_frame, image=stop_btn, borderwidth=0, command=stop).grid(row=0, column=4)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song to Playlist", command = add_song)

root.mainloop()