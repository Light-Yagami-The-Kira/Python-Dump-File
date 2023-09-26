from tkinter import *

def func0():


        ROOT = Tk()


        ROOT.geometry('300x100')

        ROOT.minsize(300, 100)

        ROOT.title('Save File')


        Label(ROOT, text='Save File As', font=(23)).grid(row=0, column=0)
        

        fileName = StringVar()


        Entry(ROOT, textvariable=fileName).grid(column=1 , row=0)


        def Savefunc():
                
                print(f'File Saved As {fileName.get()}')

                


        saveButton = Button(ROOT, text='Save', command=Savefunc)

        saveButton.grid()
        
        

        ROOT.mainloop()