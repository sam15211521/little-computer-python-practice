from tkinter import *

root = Tk()
e =Entry(root, width = 50, borderwidth=10)
e.pack()
e.insert(0, "Enter Your Name: ")



def clicking():
    hello ="Hello " +e.get()   #.get() pulls the entry from e to use as a funciton
    myLable =Label(root, text =hello)
    myLable.pack()

myButton = Button(root, text ="Enter Your Name", padx =50, pady=50, command = clicking, fg = 'blue', bg ='#000000', wraplength = 2) 
            #Button(where, text =, size in x axis, size in y axis,    command signals what will run, fg changes the color of the text, bg changes the background color)
myButton.pack()


root.mainloop()