from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('744x377')

    def status(self):
        self.var = StringVar()
        self.var.set('Ready')
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor=E)
        self.statusbar.pack(side=BOTTOM, fill=X)

    def createButton(self, inpText):
        def func():
            print(f'Button {inpText} clicked')
        Button(self, text=inpText, command=func).pack()

if __name__ == "__main__":
    window = GUI()
    window.status()
    window.createButton('Submit')
    window.mainloop()