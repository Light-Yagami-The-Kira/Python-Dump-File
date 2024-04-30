from tkinter import *
root = Tk()
root.geometry("655x433")
f1 = Frame(root, bg="red", borderwidth=5, relief=SUNKEN)
f1.pack(side=TOP, fill=X, padx=34)
l = Label(f1, text="Project Tkinter")
l.pack(pady=43, padx=10)
root.mainloop()
