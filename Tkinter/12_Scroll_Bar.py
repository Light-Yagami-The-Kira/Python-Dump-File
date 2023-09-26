from tkinter import *

root = Tk()
frame = Frame(root, bg='red')
frame.pack()
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

scrollX = Scrollbar(frame, orient=HORIZONTAL)
scrollX.pack(side=BOTTOM, fill=X)

listbox = Listbox(frame, yscrollcommand=scroll.set, xscrollcommand=scrollX.set)
listbox.pack()
listbox.insert(END, 'Hajwhfjisohdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
for i in range(1,101):
    listbox.insert(END, f'item {i}')
scroll.config(command=listbox.yview)
# listbox.config(xscrollcommand=scrollX.set)  # Configure xscrollcommand

scrollX.config(command=listbox.xview)  # Configure command for horizontal scrollbar

root.mainloop()
