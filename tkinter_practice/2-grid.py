from tkinter import *

root = Tk()
# creating a Label Widget
myLabel1 = Label(root, text="Hello World!").grid(row =0, column = 0)
myLabel2 = Label(root, text="Well now! I am Sam Hendrix").grid(row =1, column =5)

# .grid will move text into rows and columns starting from 0 for each. 
# text stays in the same position
#myLabel1.grid(row =0, column = 0)
#myLabel2.grid(row =1, column =5)


root.mainloop()