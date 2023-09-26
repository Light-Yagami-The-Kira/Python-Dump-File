from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(500, 400)
root.title('Canvas')

canvasWidget = Canvas(root, width=500, height=400)
canvasWidget.pack()
canvasWidget.create_line(0,0,500,200, fill='red', width=10)
canvasWidget.create_rectangle(0,0,250,200, fill='red')
canvasWidget.create_text(250,200,text='Python')
# canvasWidget.create_oval(0,0,250,200,fill='black')
canvasWidget.create_polygon(0,0,100,200,300,400, fill='black')

root.mainloop()