from tkinter import *

window = Tk()

hello = Label(text = "Hello What is your name?", bg="black",fg='white')
name_box = Entry()
enter_button = Button(bg = "DarkBlue", fg = 'white', text="Enter")

hello.pack()
name_box.pack()
enter_button.pack()


name = name_box.get()

window.mainloop()

print(name)