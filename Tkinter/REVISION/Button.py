from tkinter import *
root = Tk()
root.geometry("655x433")

frame = Frame(root, borderwidth=4, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Print Now", command=lambda: print("Printed"))
b1.pack(side=LEFT, padx=23)
b2 = Button(frame, fg="red", text="Scan Now", command=lambda: print("Scanned"))
b2.pack(side=LEFT, padx=23)
b3 = Button(frame, fg="red", text="Hack Now", command=lambda: print("Hacked"))
b3.pack(side=LEFT, padx=23)

root.mainloop()
