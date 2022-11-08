import pandas as pd
import random
from tkinter import*

class hello:
    def new (self):
        self.window.destroy()
        hello()
    def __init__(self):
        self.window = Tk()
        self.var = random.randint(0,1000)
        self.label = Label(text = self.var)
        self.label.pack()
        self.button = Button(text= "Presiona", command=self.new)
        self.button.pack()
        self.window.mainloop()
hello()
