from tkinter import *
from Login import Login

class NewAccount:

    def on_enter(self, e):
        
    def __init__(self):
        self.window = Tk()
        self.window.title("Crea tu cuenta")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.label = Label(self.window, text="Crea tu cuenta", font=("Arial, 50"))
        self.label.pack()
        self.box1 = Entry(self.window, textvariable="Usuario", width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box1.place(x=365,y=170)
        self.box2 = Entry(self.window, textvariable= "Contraseña", width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11))
        self.box2.config(show= "*")
        self.box2.place(x=365, y=230)

        self.window.mainloop()

hola = NewAccount()
