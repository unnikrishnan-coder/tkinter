import pyttsx3 as tts
import os
import tkinter as tk
from tkinter import *
import time

engine = tts.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('volume',2)
engine.setProperty('voice', voices[1])
def intro():
    time.sleep(2)
    engine.say('this is an artificial intelligence based software. please tell me what to do')
    engine.runAndWait()
    
root = tk.Tk()

intro()

def speech():
            global speech_entry
            text = speech_entry.get()
            speech_entry.delete(0, END)
            engine.say(str(text))
            engine.runAndWait()
            
            

speech_label = Label(root, text='type what you want')
speech_label.grid(row=0, column=0, columnspan=3)
speech_entry = tk.Entry(root)
speech_entry.grid(row=1,column=1)
speech_button = Button(root, text='i will speak', command=speech)
speech_button.grid(row=2, column=1, columnspan=3)


root.mainloop()