from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(500, 400)

user = Label(text='Username')
password = Label(text='Password')

user.grid(column=0, row=0)
password.grid(column=0, row=1)




root.mainloop()