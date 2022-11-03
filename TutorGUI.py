from tkinter import*
class tutorGUI:
    def gotoAddTutor():
        pass
    def gotoAddSource():
        pass
    def __init__(self):
        self.window = Tk()
        self.window.title("Select an option")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.label = Label(self.window, text="¿Que quieres hacer?", font=("Arial", 50))
        self.label.pack()
        self.button1 = Button(self.window, text="Agregar tutor")
        self.button1.place(x=300, y=200)
        self.button2 = Button(self.window, text = "Agregar recursos")
        self.button2.place(x=500, y=200)
        self.window.mainloop()

hey = tutorGUI()