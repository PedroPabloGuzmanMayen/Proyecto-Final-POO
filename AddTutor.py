from tkinter import *
from AddData import AddData
import pandas as pd
class AddTutor:

    def addTutor(self):
        self.add = AddData()
        data = pd.read_excel("Tutors.xlsx")
        self.add.newTutor(self.box1.get(), self.box3.get(), self.box2.get(), data)
        self.box1.delete(0, END)
        self.box2.delete(0, END)
        self.box3.delete(0, END)
    def __init__(self):
        self.window = Tk()
        self.window.title("Agrgega un tutor")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.label1 = Label(self.window, text="Agrega un tutor", font=("Arial", 50))
        self.label1.pack()
        self.frame = Frame(self.window, width=350, height=390)
        self.frame.place(x=300, y =100)
        self.label2 = Label(self.frame, text="Nombre del tutor")
        self.label2.pack()
        self.box1 = Entry(self.frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box1.pack()
        self.label3 = Label(self.frame, text="Email del tutor")
        self.label3.pack()
        self.box2 = Entry(self.frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box2.pack()
        self.label3 = Label(self.frame, text="Numero de telefono del tutor")
        self.label3.pack()
        self.box3 = Entry(self.frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box3.pack()
        self.button = Button(self.frame, text="Agregar tutor!", command=self.addTutor)
        self.button.pack()
        self.window.mainloop()
AddTutor()