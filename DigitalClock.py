import tkinter as tk
from time import strftime

def time():
    t=strftime("%H:%M:%S %p \n %D")
    label.config(text=t)
    label.after(1000,time)

root=tk.Tk()
root.title("Digital Clock")

label=tk.Label(root,font=('calibri',50,'bold'),background='cyan',foreground='black')
label.pack(anchor='center')

time()
root.mainloop()