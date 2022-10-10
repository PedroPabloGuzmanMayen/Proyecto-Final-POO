import pandas as pd
import random
class user():
    pass

class player(user):
    pass

class tutor(user):
    pass

class logic():
    condition = True
    def game(self, preguntas):
        #questions = preguntas["Pregunta"].unique
        #answers = preguntas["Respuesta"].unique
        
        while self.condition:
            question1 = random.choice(preguntas["Pregunta"])
            print("Pregunta: " + question1)
            print()
            answer1 = input("Ingrese su respuesta: ")
            
            if answer1 not in preguntas["Respuesta"].unique():
                print("Incorrecto")
                self.condition = False
            else:
            
                for i in range(len(preguntas)):
                    if preguntas.loc[i]["Pregunta"] == question1 and answer1 == preguntas.loc[i]["Respuesta"]:
                        print("Correcto")
                
                    

class main():
    pass

class database():
    questionslvl1 = pd.read_csv("preguntas_preprimaria.csv")

l = logic()
d = database()

l.game(d.questionslvl1)