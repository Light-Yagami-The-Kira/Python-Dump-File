from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(500, 400)
root.title('Username Submission Form')


''' Form Starts Here '''

userValue = StringVar()
passValue = StringVar()
userInput = Entry(textvariable=userValue)
passInput = Entry(textvariable=passValue)

user = Label(text='Username')
password = Label(text='Password')

user.grid(row=0, column=0)
password.grid(row=1, column=0)

userInput.grid(row = 0, column=1)
passInput.grid(row=1, column=1)


def submit():
    username = userValue.get()
    password = passValue.get()

    print(f'Username : {username}\nPassword : {password}\n.........has been registered')

    with open('log.txt', 'a') as f:
        f.write(f'Username : {username}--Password : {password} has been registered\n')


Button(text='Submit', command=submit).grid()


root.mainloop()