# import necessary libraries 
from tkinter import *
from tkinter import messagebox

# setup tkinter window
root = Tk()
root.geometry("200x200")

# function for displaying warning message
# this will be called once the button is clicked
# messagebox.showwarning("window name", "text to be dispayed")
def msg():
        messagebox.showwarning("aleart", "stop! virus found.")

# adding button widget to window
button = Button(root, text="scan for virus", command=msg)
button.place(x=40, y=80)

# entering main event loop
root.mainloop()
