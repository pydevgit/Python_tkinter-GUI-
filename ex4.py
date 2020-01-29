# linked button and label
from tkinter import *
root = Tk()

myLabel = Label(root, textvariable="labelText")
myLabel.pack()


def change_red():
    labelText.set("Red")
    myLabel.config(bg="red")


labelText = StringVar()
# define more button
myButton = Button(root, bg="Red", command=change_red).pack()
root.mainloop()
