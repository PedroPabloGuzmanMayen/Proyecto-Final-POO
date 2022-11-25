from tkinter import*
import random
import pandas as pd
from user import user
from AddData import AddData
class questions:

    def nextButton(self):
        self.window.destroy()
        self.question_list.clear()
        questions(self.us)


    def __init__(self, user):
        self.window = Tk()
        self.us = user
        self.add = AddData()
        self.questions = self.add.getQuestions(self.us.getscore())
        self.numb = random.randint(0, len(self.questions))
        
        self.question_list = []
        self.question_list.append(self.questions.loc[self.numb]["Answer"])
        self.question_list.append(self.questions.loc[self.numb]["Option1"])
        self.question_list.append(self.questions.loc[self.numb]["Option2"])
        self.question_list.append(self.questions.loc[self.numb]["Option3"])
        self.label = Label(self.window, text=self.questions.loc[self.numb]["Question"], font =("Arial", 35))
        self.label.pack()
        random.shuffle(self.question_list)
        self.window.title("Juego de preguntas")
        self.message = Label(self.window, text = "Desafía tus conocimientos")
        self.message.pack()
        self.questionmessage = Label(self.window, text= self.questions.loc[self.numb]["Question"])
        self.questionmessage.pack()
        self.answer = StringVar()
        for i in range(len(self.question_list)):
            self.radiob = Radiobutton(self.window, text = self.question_list[i], variable = self.answer, value = i)
            self.radiob.pack()
        self.nextbutton = Button(self.window, text="Siguiente", command= self.nextButton)
        self.nextbutton.place(x=425, y =300)
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.window.mainloop()
        print(self.us.getusername())
        self.us.setscore(self.us.getscore()+20)
   

        print(self.us.getscore())

hola = user()
hola.setusername("adios")
hola.setscore(400)
questions(hola)