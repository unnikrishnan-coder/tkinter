import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()



rest = 1
def next(num):
    global image_no
    global btn
    global btn_2
    global my_label
    image_no += 1
    status = Label(root, text=f'image {image_no} of {len(img_list)}', bd=1, relief=SUNKEN)
    status.grid(row=2, column=2, columnspan=3)
    my_label.grid_forget()
    my_label = Label(root, image=img_list[num-1])
    my_label.grid(row=0,column=0,columnspan=3)
    btn_2 = Button(root, text='previous', command=lambda:previous(num-1)).grid(row=1, column=2)
    global rest
    rest += 1
    
    if rest > 8:
        btn = Button(root, text='next', state= DISABLED)
        btn.grid(row=1, column=0)
    else:
        btn = Button(root, text='next', command=lambda: next(num+1))
        btn.grid(row=1, column=0)
        
        
      
def previous(num):
    global btn
    global btn_2
    global my_label
    global image_no
    image_no -= 1
    status = Label(root, text=f'image {image_no} of {len(img_list)}', bd=1, relief=SUNKEN)
    status.grid(row=2, column=2, columnspan=3)
    my_label.grid_forget()
    my_label = Label(root, image=img_list[num-1])
    my_label.grid(row=0,column=0,columnspan=3)
    btn_2 = Button(root, text='previous', command=lambda:previous(num-1)).grid(row=1, column=2)
    global rest
    rest -= 1
    
    if rest < 1:
        btn_2 = Button(root, text='previous', state= DISABLED)
        btn_2.grid(row=1, column=2)
    else:
        btn_2 = Button(root, text='previous', command=lambda: previous(num-1))
        btn.grid(row=1, column=2)
    
    
    
img_1 = Image.open("C://Users//DELL//Desktop//tkinter//images//unni.jpg")
img_3 = Image.open("C://Users//DELL//Desktop//tkinter//images//2.jpg")
img_2 = Image.open("C://Users//DELL//Desktop//tkinter//images//1.jpg")
img_4 = Image.open("C://Users//DELL//Desktop//tkinter//images//3.jfif")
img_5 = Image.open("C://Users//DELL//Desktop//tkinter//images//4.jpg")
img_6 = Image.open("C://Users//DELL//Desktop//tkinter//images//5.jpg")
img_7 = Image.open("C://Users//DELL//Desktop//tkinter//images//6.jpg")
img_8 = Image.open("C://Users//DELL//Desktop//tkinter//images//7.jpg")

img_1 = img_1.resize((250, 250), Image.ANTIALIAS)
img_2 = img_2.resize((250, 250), Image.ANTIALIAS)
img_3 = img_3.resize((250, 250), Image.ANTIALIAS)
img_4 = img_4.resize((250, 250), Image.ANTIALIAS)
img_5 = img_5.resize((250, 250), Image.ANTIALIAS)
img_6 = img_6.resize((250, 250), Image.ANTIALIAS)
img_7 = img_7.resize((250, 250), Image.ANTIALIAS)
img_8 = img_8.resize((250, 250), Image.ANTIALIAS)

IMG_8 = ImageTk.PhotoImage(img_1)
IMG_7 = ImageTk.PhotoImage(img_2)
IMG_6 = ImageTk.PhotoImage(img_3)
IMG_5 = ImageTk.PhotoImage(img_4)
IMG_4 = ImageTk.PhotoImage(img_5)
IMG_3 = ImageTk.PhotoImage(img_6)
IMG_2 = ImageTk.PhotoImage(img_7)
IMG_1 = ImageTk.PhotoImage(img_8)

img_list = [IMG_1, IMG_2, IMG_3, IMG_4, IMG_5, IMG_6, IMG_7, IMG_8]

image_no = 1

status = Label(root, text=f'image {image_no} of {len(img_list)}', bd=1, relief=SUNKEN)
status.grid(row=2, column=2, columnspan=3, sticky="w"+"e")
btn = Button(root, text='next', command=lambda: next(2))
btn.grid(row=1, column=0)
btn_2 = Button(root, text='previous', command=previous, state= DISABLED).grid(row=1, column=2)
my_label = Label(root, image=IMG_8)
my_label.grid(row=0,column=0,columnspan=3)

root.mainloop()
