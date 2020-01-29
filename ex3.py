from tkinter import *
# import messagebox by tkinter
from tkinter import messagebox
root = Tk()
# define a buttonClicked function
def buttonClicked():
    messagebox._show("Message", "Button Clicked")

# define a button and said button click me and command below side
myButton = Button(root, text="click me!", command=buttonClicked)
myButton.pack()

root.mainloop()