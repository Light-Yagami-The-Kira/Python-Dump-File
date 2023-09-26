from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(500, 400)

user = Label(text='Username')
password = Label(text='Password')

user.grid(column=0, row=0)
password.grid(column=0, row=1)


def getValue():
    print(userValue.get(), passValue.get()) 


userValue = StringVar()
passValue = StringVar()

userEntry = Entry(textvariable=userValue)
passEntry = Entry(textvariable=passValue)

userEntry.grid(column=1, row=0)
passEntry.grid(column=1, row=1)

Button(root, text='Submit', command=getValue).grid()

root.mainloop()