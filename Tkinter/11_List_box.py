from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack()
listbox.insert(END, 'First Item')

userInput = StringVar()

Label(text='Enter Input to Add in the list').pack()
Entry(textvariable=userInput).pack()

Button(text='ADD', command = lambda : listbox.insert(END, userInput.get())).pack()

root.mainloop()