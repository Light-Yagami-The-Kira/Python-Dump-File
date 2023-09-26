from tkinter import *

root = Tk()

root.geometry('1000x900')
root.minsize(1000, 900)
root.title('Menus')
n = StringVar()

'''TODO:Functions'''
def new():
    print('A new file has been created')
def Save():
    ROOT = Tk()
    ROOT.geometry('300x100')
    ROOT.minsize(300, 100)
    ROOT.maxsize(300, 100)
    ROOT.title('Save File with Name')

    Label(ROOT,text='Name', font=('Arial', 28)).pack(fill=X)
    
    def returnFileName(n1):
        
        print(f'File has been saved with name {n1.get()}')


    Entry(ROOT,textvariable=n).pack(fill=X)

    saveButton = Button(ROOT,text='Save', command=lambda : returnFileName(n))
    # saveButton.bind('<Button-1>', quit)
    saveButton.pack()

    ROOT.mainloop()
"""_______________________________________________________________________"""

Label(text='Thank You for using our website.', bg='red', font=('Sunshine Olivia', 48, 'bold', 'italic', 'underline')).pack(fill=X)

menubar = Menu(root)

FileMenu = Menu(menubar)
FileMenu.add_command(label='New', command=new)
FileMenu.add_separator()
FileMenu.add_command(label='Save', command=Save)
FileMenu.add_separator()


menubar.add_cascade(label='File', menu=FileMenu)
root.config(menu=menubar)
root.mainloop()