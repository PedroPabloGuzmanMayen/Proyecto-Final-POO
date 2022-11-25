from QuestionGUI import questions
from GameGUI import game
from ResoucresGUI import Resources
from CompareScoreGUI import compareScore
from ShowTutorsGUI import ShowTutors
from tkinter import*
class ConfirmationWindow:

    def __init__(self, number, us):
        self.user = us
        self.window = Tk()
        self.window.title("Confirmation Window")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.confirmButton = Button(text="Confirmar")
        self.confirmButton.pack()
        if number ==1:
            questions(self.user)
        elif number == 2:
            game()
        elif number == 3:
            compareScore()
        elif number == 4:
            Resources()
        elif number == 5:
            ShowTutors()
