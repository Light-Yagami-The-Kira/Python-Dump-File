from tkinter import *

root = Tk()
root.geometry("600x400")

root.title("My Title")

## IMPORTANT LABEL OPTIONS
"""
text - adds the text
bd - background
fg - foreground
font - sets the font 
padx - x padding
pady - y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE 
"""
f = open("gojo.txt", "r")
content = f.read()
f.close

a = StringVar()
a.set(content)

title_label = Label(root, textvariable=a, bg="black", foreground="white",padx=10, font=("comicsansms", 23, "bold"), borderwidth=3, relief=SUNKEN)
title_label.pack()

q = Label(root, text="q", background="yellow")
q.pack(anchor="se", side=BOTTOM, fill=BOTH)
root.mainloop()