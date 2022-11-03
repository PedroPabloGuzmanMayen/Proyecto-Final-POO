from tkinter import *
from user import user
from QuestionGUI import questions
from GameGUI import game
from ResoucresGUI import Resources
from CompareScoreGUI import compareScore
class menu:

    def gotToQuestionsGUI(self):
        self.window.destroy()
        questions()
    def goToGameGUI(self):
        self.window.destroy()
        game()
    def gotToScoreGUI(self):
        self.window.destroy()
        questions()
    def goToAddTutorGUI(self):
        pass
    def goToResources(self):
        pass

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
        self.buttonquestions.place(x =20, y=50)
        self.buttonscore = Button(self.window, text="Comparar puntaje")
        self.buttongame = Button(self.window, text="Juego de habilidad mental")
        self.buttonresource = Button(self.window, text="Recursos educativos")
        self.buttontutors = Button(self.window, text="Buscar un tutor")

        print(self.user.getscore())
        print(self.user.getusername())
        self.window.mainloop()


        