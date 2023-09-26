from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(500, 400)
root.title('Image Description')

Label(root, text='Image Description', bg='red', font=('Goudy Stout', 28, 'bold', 'italic', 'underline')).pack(fill=X)

frame0 = Frame(root, bg='blue')
frame0.pack(fill=X, anchor=W)

png1 = Label(frame0, image=PhotoImage(file='png1.png'), anchor=E)
png1.pack(side=LEFT)

with open('png1.txt', 'r') as f:
    png1Content = f.read()

Label(frame0, text=png1Content, bg='red', font=400).pack(side=LEFT, fill=X)

root.mainloop()