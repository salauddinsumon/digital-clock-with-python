
from time import strftime
from tkinter import *


root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S ')
    label.config(text=string)
    label.after(1000,time)


label= Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()
