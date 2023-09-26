
'''
text - adds text
image - adds image
bd - decides background
fg - decides foreground
font - sets font
padx - x padding
pady - y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
borderwidth
'''

from tkinter import *

root = Tk()

root.geometry('1000x500')

root.minsize(400,400)
root.maxsize(1400,1000)

root.title("This is title line.")

string = Label(text='This a label text of Tkinter GUI.',fg='red',padx=100,pady=100,borderwidth=50,relief='sunken',font=('Arial',23,'bold','italic','underline'))

'''
anchor - n,nw,ne,e,w,s...... {north,south.....}
side - top,bottom,left,right
fill - 
padx - 
pady - 
'''


string.pack(side='bottom',anchor='e',fill=X)

root.mainloop()





