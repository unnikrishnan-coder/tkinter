import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Calculator')
# root.geometry('290x430')


def calc(val):
    num = e.get()
    e.delete(0, END)
    e.insert(0, str(num)+str(val))


def clear():
    e.delete(0, END)


def plus():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    global expression
    expression = "+"
    f_num = str(first_num)

def minus():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    global expression
    expression = "-"
    f_num = str(first_num)
    
def into():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    global expression
    expression = "*"
    f_num = str(first_num)
    
def div():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    global expression
    expression = "/"
    f_num = str(first_num)

def equal():
    second_num = str(e.get())
    e.delete(0, END)
    try:
        result = eval(f"{f_num}{expression}{second_num}")
        e.insert(0, result)
    except :
        e.insert(0, 'error:clear the screen and try another one')
    

e = Entry(root, borderwidth=5, width=38)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, text='1', padx=10, pady=10, borderwidth=5,command=lambda: calc(1)).grid(row=2, column=0)
button_2 = Button(root, text='2', padx=10, pady=10, borderwidth=5,command=lambda: calc(2)).grid(row=2, column=1)
button_3 = Button(root, text='3', padx=10, pady=10, borderwidth=5,command=lambda: calc(3)).grid(row=2, column=2)
button_4 = Button(root, text='4', padx=10, pady=10, borderwidth=5,command=lambda: calc(4)).grid(row=3, column=0)
button_5 = Button(root, text='5', padx=10, pady=10, borderwidth=5,command=lambda: calc(5)).grid(row=3, column=1)
button_6 = Button(root, text='6', padx=10, pady=10, borderwidth=5,command=lambda: calc(6)).grid(row=3, column=2)
button_7 = Button(root, text='7', padx=10, pady=10, borderwidth=5,command=lambda: calc(7)).grid(row=4, column=0)
button_8 = Button(root, text='8', padx=10, pady=10, borderwidth=5,command=lambda: calc(8)).grid(row=4, column=1)
button_9 = Button(root, text='9', padx=10, pady=10, borderwidth=5,command=lambda: calc(9)).grid(row=4, column=2)
button_0 = Button(root, text='0', padx=10, pady=10, borderwidth=5,command=lambda: calc(0)).grid(row=5, column=1)

button_equal = Button(root, text='=', padx=40, pady=4, borderwidth=5,command=equal).grid(row=6, columnspan=4)
button_clear = Button(root, text='cls', padx=10, pady=10, borderwidth=5, command=clear).grid(row=5, column=0)

button_plus = Button(root, text='+', padx=10, pady=10, borderwidth=5,command=plus).grid(row=1, column=0,)
button_minus = Button(root, text='-', padx=10, pady=10, borderwidth=5,command=minus).grid(row=1, column=1)
button_x = Button(root, text='x', padx=10, pady=10, borderwidth=5,command=into).grid(row=1, column=2)
button_div = Button(root, text='/', padx=10, pady=10, borderwidth=5,command=div).grid(row=5, column=2)

root.mainloop()
