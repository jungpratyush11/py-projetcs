import tkinter as tk
from tkinter import filedialog

root=tk.Tk()
root.title("Text Editor")
root.geometry("700x500")

text_area=tk.Text(root,font=("Arial",14))
text_area.pack(expand=True,fill="both")

def new_file():
    text_area.delete("1.0",tk.END)
    
def open_file(): 
    file=filedialog.askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if file:
        with open(file,"r") as f:
            text_area.delete("1.0",tk.END)
            text_area.insert(tk.END,f.read())
            
def save_file():
    file=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if file:
        with open(file,"w") as f:
            f.write(text_area.get("1.0",tk.END))
            
menu_bar=tk.Menu(root)
root.config(menu=menu_bar)

file_menu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)


file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

root.mainloop()