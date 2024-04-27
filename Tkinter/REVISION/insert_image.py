from tkinter import *
from PIL import Image, ImageTk

root = Tk() # Basic GUI Loader

root.geometry("720x500")
root.minsize(400, 400)
root.maxsize(900, 600)

photo_data = PhotoImage(file="gojo.png")
image = Label(image=photo_data)
image.pack()

photo_data2 = PhotoImage(file="gojo.jpg")
image2 = Label(image=photo_data2)
image2.pack()



root.mainloop()