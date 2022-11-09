from tkinter import*
import random
import pandas as pd
class questions:
    def __init__(self, user):
        self.window = Tk()
        if (self.us.getscore() <= 500):
            self.questions = 2
        if ( 500 < self.us.getscore() <= 1000):
            self.questions = 1
        if (1000 < self.us.getscore() <= 1500):
            self.questions = 3
        if (1500 < self.us.getscore() <=2000):
            self.questions = 4
        self.question = random.randint(0,100)
        self.answer = StringVar()
        
        self.window.title("Juego de preguntas")
        self.us = user
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.window.mainloop()
        print(self.us.getusername())
        self.us.setscore(self.us.getscore()+20)

        print(self.us.getscore())