from tkinter import *
root = Tk()
statusVar = StringVar()
statusVar.set('Ready')
sbar = Label(textvariable=statusVar, relief=SUNKEN, borderwidth=10, anchor=E)
sbar.pack(fill=X, side=BOTTOM)
def update():
    statusVar.set('Busy...')
    sbar.update()
    import time
    time.sleep(3)
    for i in range(3,0,-1):
        statusVar.set(f'Almost Done in {i}')
        sbar.update()
        time.sleep(1)  
    statusVar.set('Ready')
    sbar.update()
Button(root, text='UPDATE', command=update, anchor=E).pack(side=BOTTOM)
root.mainloop()