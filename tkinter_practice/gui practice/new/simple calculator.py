from re import match
from tkinter import *
from typing import Match


#functions

def checking():
    if calculations == True:
        data_box.delete(0,END)
        calculations = False
    else:
        print("Opps")

def button_adding():
    num1 = data_box.get()
    global number1
    global math
    math = 'addition'
    number1 = int(num1)
    data_box.delete(0,END)
    

def subtracting_button():
    num1 = data_box.get()
    global number1
    global math
    math = 'subtraction'
    number1 = int(num1)
    data_box.delete(0,END)

def dividing_button():
    num1 = data_box.get()
    global number1
    global math
    math = 'division'
    number1 = int(num1)
    data_box.delete(0,END)

def multiplication_button():
    num1 = data_box.get()
    global number1
    global math
    math = 'multiplication'
    number1 = int(num1)
    data_box.delete(0,END)
        
def button_click(number):
    
    current= data_box.get()
    data_box.delete(0,END)
    data_box.insert(0, str(current) + str(number))

def clear_button():
    data_box.delete(0, END)


def equal_button():                     #defines what happens when the = button is pressed
    num2 = data_box.get()
    data_box.delete(0,END)
    global calculations
    calculations = True 
    

    if math == 'addition':
        data_box.insert(0,number1 + int(num2))
    elif math == 'subtraction':
        data_box.insert(0, number1 - int(num2))
    elif math == 'multiplication':
        data_box.insert(0, number1 *int(num2))
    elif math == 'division':
        data_box.insert(0, number1 / int(num2))



root = Tk()
root.title("Simple Calculator")




# defining Buttons
data_box = Entry(root, width = 50, borderwidth=5 )
button1 = Button(root, text = '1', width=10, height=5, command=lambda: [checking, button_click(1)])
button2 = Button(root, text = '2', width=10, height=5, command=lambda: [checking, button_click(2)])
button3 = Button(root, text = '3', width=10, height=5, command=lambda: [checking, button_click(3)])
button4 = Button(root, text = '4', width=10, height=5, command=lambda: [checking, button_click(4)])
button5 = Button(root, text = '5', width=10, height=5, command=lambda: [checking, button_click(5)])
button6 = Button(root, text = '6', width=10, height=5, command=lambda: [checking, button_click(6)])
button7 = Button(root, text = '7', width=10, height=5, command=lambda: [checking, button_click(7)])
button8 = Button(root, text = '8', width=10, height=5, command=lambda: [checking, button_click(8)])
button9 = Button(root, text = '9', width=10, height=5, command=lambda: [checking, button_click(9)])
button0 = Button(root, text = '0', width=10, height=5, command=lambda: [checking, button_click(0)])

#function buttons
button_clear = Button(root, text = "Clear", width = 20, height=5 ,command=clear_button)
button_addition = Button(root, text = "+", width = 10, height=5, command= button_adding)
button_equal = Button(root, text = "=", width = 10, height=10, borderwidth=4, bg = 'gray', command=equal_button)
button_multiply = Button(root, text = "X", width = 10, height = 5, command = multiplication_button)
button_divide = Button(root, text = "/", width = 10, height = 5, command =  dividing_button)
button_subtraction =Button(root, text = "-", width = 10, height = 5, command =  subtracting_button)


#putting screen on calculator

data_box.grid(column=1,row=1,columnspan=3)

#putting buttons on the calculator

button1.grid(column=1,row=4)
button2.grid(column=2,row=4)
button3.grid(column=3,row=4)
button4.grid(column=1,row=3)
button5.grid(column=2,row=3)
button6.grid(column=3,row=3)
button7.grid(column=1,row=2)
button8.grid(column=2,row=2)
button9.grid(column=3,row=2)
button0.grid(column=1,row=5)

button_addition.grid(column = 1, row = 6)
button_subtraction.grid(column = 2, row=6)
button_multiply.grid(column=3,row=6)
button_divide.grid(column=4, row=6)

button_equal.grid(column = 4, row = 4, rowspan=2)
button_clear.grid(column= 2, row=5, columnspan= 2)


root.mainloop()


