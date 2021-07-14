from tkinter import *

root = Tk()

def square():
    myLable =Label(root, text ="Look! I can click Buttons!")
    myLable.pack()

myButton = Button(root, text ="Click Me!", padx =50, pady=50, command = square, fg = 'blue', bg ='#000000') 
            #Button(where, text, size in x axis, size in y axis,    command signals what will run, fg changes the color of the text, bg changes the background color)
myButton.pack()


root.mainloop()