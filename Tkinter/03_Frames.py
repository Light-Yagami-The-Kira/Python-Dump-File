from tkinter import *

root = Tk()
root.geometry('500x400')
root.minsize(500, 400)

frame_1 = Frame(root, bg='black', borderwidth=10)
frame_1.pack(side='top', fill=X)

text = Label(frame_1, text='Hello World in frame', bg='black', fg='red')
text.pack()

root.mainloop()
