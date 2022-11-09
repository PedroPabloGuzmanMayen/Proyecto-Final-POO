import random 
import pandas as pd
'''
import pandas as pd
import random
from tkinter import*

class hello:
    def new (self):
        self.window.destroy()
        hello()
    def __init__(self):
        self.window = Tk()
        self.var = random.randint(0,1000)
        self.label = Label(text = self.var)
        self.label.pack()
        self.button = Button(text= "Presiona", command=self.new)
        self.button.pack()
        self.window.mainloop()
hello()
'''

list = [1,2,3,4]

random.shuffle(list)
print(list)
random.shuffle(list)
print(list)
random.shuffle(list)
print(list)
random.shuffle(list)
print(list)
print(list)
random.shuffle(list)
print(list)
print(list)
random.shuffle(list)
print(list)

hola = pd.read_excel("Questions.xlsx")

print(hola["Option1"])

adios = 50

hola.at[4, "Option1"] = adios

tankev = hola["Option1"].sample()

hola.to_excel("Resources.xlsx", index = False)