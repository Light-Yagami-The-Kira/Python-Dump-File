from tkinter import *
import h

root = Tk()

root.geometry('500x400')
root.minsize(500, 400)

root.title('Microsoft Word')

def Save():
    ROOT = Tk()

    ROOT.geometry('300x100')
    ROOT.minsize(300, 100)
    ROOT.title('Save File')

    Label(ROOT, text='Save File As', font=(23)).grid(row=0, column=0)
    
    global fileName
    fileName = StringVar()

    Entry(ROOT, textvariable=fileName).grid(column=1 , row=0)

    def Savefunc():
        global fileName
        print(f'File Saved As {fileName.get()}')

        quit

    saveButton = Button(ROOT, text='Save', command=Savefunc)
    saveButton.grid()
    
   
    ROOT.mainloop()


MenuBar = Menu(root)


FileMenu = Menu(MenuBar, tearoff=0)

FileMenu.add_command(label='Save', command=Save)

MenuBar.add_cascade(label='File', menu=FileMenu)

root.config(menu=MenuBar)
root.mainloop()