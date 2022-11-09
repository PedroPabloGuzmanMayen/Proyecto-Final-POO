from tkinter import*
from AddTutor import AddTutor
from AddSource import AddSourceGUI
class tutorGUI:
    def gotoAddTutor(self):
        self.window.destroy()
        AddTutor("Agregar un tutor", "Nombre del tutor", "Correo del tutor", "Telefono del tutor", "Agregar tutor!")
    def gotoAddSource(self):
        AddSourceGUI("Agregar un recurso", "Nombre del recurso", "Nivel del recurso", "Tematica del recurso", "Agregar el recurso!")
    def __init__(self):
        self.window = Tk()
        self.window.title("Select an option")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.label = Label(self.window, text="¿Que quieres hacer?", font=("Arial", 50))
        self.label.pack()
        self.button1 = Button(self.window, text="Agregar tutor", command= self.gotoAddTutor)
        self.button1.place(x=300, y=200)
        self.button2 = Button(self.window, text = "Agregar recursos", command= self.gotoAddSource)
        self.button2.place(x=500, y=200)
        self.window.mainloop()

