from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(500,400)
root.title('Title Line')


# Label(text='This a normal text in a frame', bg='red').grid()

userValue = StringVar()

age_over_18 = IntVar()

Label(text='Username').grid(row=0, column=0)
Entry(textvariable=userValue).grid(row=0, column=1)

Checkbutton(text='Age Over 18', variable=age_over_18).grid()

def submission():
    print(userValue.get(), age_over_18.get())

Button(text='Submit', command=submission).grid()

root.mainloop()