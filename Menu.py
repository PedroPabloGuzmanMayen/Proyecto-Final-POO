from tkinter import *
class menu:
    def __init__(self):
        self.window = Tk()
        self.label = Label(self.window, text= "Hola mundo")
        self.label.pack()
        self.window.mainloop()
        