from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(500, 400)
root.title('Radio Button')

var = IntVar()

radio = Radiobutton(root, text='Text Piece', variable=var, value=1).pack()

radio = Radiobutton(root, text='Text Piece2', variable=var, value=2).pack()




root.mainloop()