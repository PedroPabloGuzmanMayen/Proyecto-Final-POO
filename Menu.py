from tkinter import *
from user import user
from QuestionGUI import questions
from GameGUI import game
from ResoucresGUI import Resources
from CompareScoreGUI import compareScore
from ShowTutorsGUI import ShowTutors
from DiagnosisGUI import diagnosis
class menu:

    def gotToQuestionsGUI(self):
        self.window.destroy()
        questions(self.user)
    def goToGameGUI(self):
        self.window.destroy()
        diagnosis(self.user, 0)
    def gotToScoreGUI(self):
        self.window.destroy()
        compareScore()
    def goToResources(self):
        self.window.destroy()
        Resources()
    def goToTutors(self):
        self.window.destroy()
        ShowTutors()

    def __init__(self, name, score):
        self.user = user()
        self.user.setusername(name)
        self.user.setscore(score)
        self.window = Tk()
        self.window.title("Menu")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.label = Label(self.window, text= "¿Que quieres hacer?", font =("Arial", 50))
        self.label.pack()
        self.buttonquestions = Button(self.window, text="Juego de preguntas", command = self.gotToQuestionsGUI)
        self.buttonquestions.place(x =300, y=100)
        self.buttonscore = Button(self.window, text="Comparar puntaje",command = self.gotToScoreGUI )
        self.buttonscore.place(x=500, y=100)
        self.buttongame = Button(self.window, text="Examen diagnóstico")
        self.buttonscore.place(x=300, y=200)
        self.buttonresource = Button(self.window, text="Recursos educativos", command =self.goToResources)
        self.buttonresource.place(x=500, y=200)
        self.buttontutors = Button(self.window, text="Buscar un tutor", command = self.goToTutors)
        self.buttontutors.place(x=300,y=300 )
        self.window.mainloop()



        