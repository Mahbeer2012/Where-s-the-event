# import necessary libraries 
from tkinter import *

# create window 
window = Tk()
window.title("event handler")
window.geometry("100x100")

# event handler for keypass
def handler_keypass(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handler_keypass)

# Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

# blind click event to handle_click()
button.bind("<button-1>", handle_click)

window.mainloop()
