from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(500, 400)
root.title('Handling Events')

def button(event):
    print(f'You pressed button0 at {event.x}, {event.y}')

@staticmethod
def button0_():
    print('This Button0 function doesn\'t take any arguement')

button0 = Button(root, text='Button0')
button0.pack()

button0.bind('<Button-1>', button)
button0.bind('<Double-1>', quit)


root.mainloop()