from QuestionGUI import questions
from GameGUI import game
from ResoucresGUI import Resources
from CompareScoreGUI import compareScore
from ShowTutorsGUI import ShowTutors
from tkinter import*
class ConfirmationWindow:

    def next(self):
        if self.number ==1:
            self.window.destroy()
            questions(self.user)
        elif self.number == 2:
            self.window.destroy()
            game()
        elif self.number == 3:
            self.window.destroy()
            compareScore()
        elif self.number == 4:
            self.window.destroy()
            Resources()
        elif self.number == 5:
            self.window.destroy()
            ShowTutors()


    def __init__(self, number, us):
        self.user = us
        self.number = number
        self.window = Tk()
        self.window.title("Confirmation Window")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.confirmButton = Button(text="Confirmar", command=self.next())
        self.confirmButton.pack()
