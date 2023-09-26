from tkinter import *
import tkinter.messagebox as msg
root = Tk()

root.geometry('500x400')

msg.showinfo('Help', 'Body')

print(msg.askquestion('title', 'How was your experience'))

root.mainloop()