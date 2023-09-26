from tkinter import *

root = Tk()

root.geometry('700x600')

root.title('Menus')

root.minsize(700, 600)

menuBar = Menu(root, tearoff=0)


def New():
    print('You have created a new file.')

def SaveAs():
    ROOT = Tk()
    ROOT.geometry('500x400')    

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New', command=New )
fileMenu.add_separator()
fileMenu.add_command(label='Save As', command=SaveAs)

menuBar.add_cascade(label='File', menu=fileMenu)
root.config(menu=menuBar)
root.mainloop()