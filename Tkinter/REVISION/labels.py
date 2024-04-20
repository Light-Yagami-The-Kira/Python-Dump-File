from tkinter import *
root = Tk() # Basic GUI Loader
root.geometry("720x500")
root.minsize(400, 400)
root.maxsize(900, 600)

some_random_text = Label(text="Hello World")
some_random_text.pack()

root.mainloop()