from tkinter import*
import random
from tkinter import messagebox
import pandas as pd
from user import user
from AddData import AddData
class diagnosis:

    def nextButton(self):
        self.numb +=1
        if (self.numb >len(self.questions) -1):
            messagebox.showerror(message= "Terminaste el examen", title="Juego terminado")
        else:
            if (str(self.answer.get()) == str(self.questions.iloc[self.numb]["Answer"])):
                messagebox.showerror(message= "Respuesta correcta", title="Respuesta correcta")
                self.add.addScore(self.us.getusername(), 30)
                diagnosis(self.us, self.numb)
            else:
                messagebox.showerror(message= "Respuesta incorrecta", title="Respuesta inccorrecta")
                diagnosis(self.us, self.numb)

    def __init__(self, user, number):
        self.window = Tk()
        self.us = user
        self.add = AddData()
        self.questions = pd.read_excel("Questions.xlsx")
        self.numb = number
        self.question_list = []
        self.question_list.append(self.questions.iloc[self.numb]["Answer"])
        self.question_list.append(self.questions.iloc[self.numb]["Option1"])
        self.question_list.append(self.questions.iloc[self.numb]["Option2"])
        self.question_list.append(self.questions.iloc[self.numb]["Option3"])
        self.label = Label(self.window, text=self.questions.iloc[self.numb]["Question"], font =("Arial", 35))
        self.label.pack()
        random.shuffle(self.question_list)
        self.window.title("Examen diagnóstico")
        self.message = Label(self.window, text = "Exámen diagnóstico")
        self.message.pack()
        self.questionmessage = Label(self.window, text= self.questions.iloc[self.numb]["Question"])
        self.questionmessage.pack()
        self.answer = StringVar()
        for i in range(len(self.question_list)):
            self.radiob = Radiobutton(self.window, text = self.question_list[i], variable = self.answer, value = str(self.question_list[i]), command=self.nextButton)
            self.radiob.pack()
        #self.nextbutton = Button(self.window, text="Siguiente", command= self.nextButton)
        #self.nextbutton.place(x=425, y =300)
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.window.mainloop()

us = user()

us.setusername("dalas")
us.setscore(20)
diagnosis(us, 0)