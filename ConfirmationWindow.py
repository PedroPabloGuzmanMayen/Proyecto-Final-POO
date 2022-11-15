from QuestionGUI import questions
from GameGUI import game
from ResoucresGUI import Resources
from CompareScoreGUI import compareScore
from ShowTutorsGUI import ShowTutors
class ConfirmationWindow:
    def __init__(self, number, us):
        self.user = us

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
