from tkinter import *

root = Tk()

slide = Scale(root, orient=HORIZONTAL, tickinterval=5)
slide.pack(side=BOTTOM, fill=X)
slide.set(69)

Button(text='Submit', command = lambda : print(slide.get())).pack()

root.mainloop()