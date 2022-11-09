from tkinter import*
class questions:
    def __init__(self, user):
        self.window = Tk()
        self.window.title("Juego de preguntas")
        self.us = user
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.window.mainloop()
        print(self.us.getname())