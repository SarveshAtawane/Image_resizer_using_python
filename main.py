import customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os.path
app = customtkinter.CTk()
app.title("Image Resizer App")
app.geometry("800x400")
name=""
com_name=""
original_size=0
file_base_name=''
file_extension=''

label3 = customtkinter.CTkLabel(app, text="", fg_color="transparent")
label3.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
def button_function():
    n=(openfile())
    global name
    global com_name
    name=n
    c,filename=os.path.split(name)
    global original_size
    original_size=os.path.getsize(name)//1000
    label = customtkinter.CTkLabel(app, text=f"Original Size {original_size}KB", fg_color="transparent")
    label.place(relx=0.72, rely=0.2, anchor=customtkinter.CENTER)
    com_name=c
    global file_base_name
    global file_extension
    file_base_name, file_extension = os.path.splitext(filename)
    com_name=com_name+"/compressed_"+file_base_name+file_extension

def button_function2():
    progressbar = customtkinter.CTkProgressBar(app, orientation="horizontal")
    progressbar.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
    label = customtkinter.CTkLabel(app, text="", fg_color="transparent")
    label.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
    size=int(entry.get())
    im = Image.open(name)
    im1 = im.copy()
    im1.save(com_name)
    rat = im.size[0] / im.size[1]
    total=os.path.getsize(name)/1000-size
    while os.path.getsize(com_name) >= size * 1000:
        old_size = os.path.getsize(com_name)
        i =(old_size//1000-size)/total
        progressbar.set(1-i)
        app.update_idletasks()
        s = im1.size[0]
        if (old_size//1000)-size>100:
            s=s-400
        s = s - 5
        im1 = im.resize((s, int(s / rat)))
        im1.save(com_name, optimized=True)
        new_size = os.path.getsize(com_name)
        if new_size >= old_size:
                s = s - 10
    progressbar.set(1.0)
    label.configure(text=f"Image Resized to size {os.path.getsize(com_name)//1000}KB Please check same folder by the name compressed_{file_base_name}{file_extension}")


def openfile():
    return filedialog.askopenfilename()
button = customtkinter.CTkButton(master=app, text="Choose File", command=button_function)
button.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
label = customtkinter.CTkLabel(app, text="Enter The File Size in which you want to resize the given file.", fg_color="transparent")
label.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)
entry = customtkinter.CTkEntry(app, placeholder_text="Size")
entry.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
button2 = customtkinter.CTkButton(master=app, text="Resize", command=button_function2)
button2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
app.mainloop()