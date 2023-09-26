from tkinter import *

root = Tk()


root.geometry('500x400')


def b():
    print('You pressed Button 0')

frame0 = Frame(root)
frame0.pack(side='top')


'''A square button appears'''

button0 = Button(frame0, text='Button0',command=b)
button0.pack()

'''Checkbox'''

foodService = IntVar()
Checkbutton(text='Food Service', variable=foodService).pack()

def submit():
    if foodService.get() == 0:
        print('No Food Service Selected.')

    else:
        print('Food Service is selected.')

Button(text='Submit', command=submit).pack()



root.mainloop()