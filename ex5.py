# define check button

from tkinter import *
root = Tk()
myLabel = Label(root, text="Which is one you like?").pack()

# define checkbutton
for value in range(1,11):
    my_checkbutton1 = Checkbutton(root, text="One").pack()
    my_checkbutton2 = Checkbutton(root, text="Two").pack()
    my_checkbutton3 = Checkbutton(root, text="Three").pack()

root.mainloop()