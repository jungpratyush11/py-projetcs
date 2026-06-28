from itertools import cycle
from PIL import Image,ImageTk
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow")

image_paths=[
    r"C:\Users\Pratyush\Downloads\images.jpg",
    r"c:\Users\Pratyush\Downloads\download.jpg",
    r"C:\Users\Pratyush\Downloads\images (1).jpg",
    
]

image_size=(1080,1080)
pil_image=[Image.open(p).resize(image_size) for p in image_paths]
tk_image=[ImageTk.PhotoImage(img) for img in pil_image]

label=tk.Label(root)
label.pack()

slideShow=cycle(tk_image)

def update_image():
    label.config(image=next(slideShow))
    label.after(3000,update_image)
    
def start_slideshow():
    update_image()
    
play_button=tk.Button(root,text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()