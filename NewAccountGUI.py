from tkinter import *
from Login import Login
from tkinter import messagebox
from LoginGUI import loginGUI
import pandas as pd

class NewAccount:
    def ButtonEvent(self):
        us = self.box1.get()
        passw = self.box2.get()
        score0 = 0
        isT = False
        self.log = Login()
        data = pd.read_excel("users_data.xlsx")
        if self.log.newAccount(us, passw, isT, score0, data):
            self.window.destroy()
            loginGUI()
        else:
            messagebox.showerror(message= "El usuario ya existe ", title="Mensaje de error")

    def __init__(self):
        self.window = Tk()
        self.window.title("Crea tu cuenta")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.label = Label(self.window, text="Crea tu cuenta", font=("Arial, 50"))
        self.label.grid(row =0, column=114)
        self.label2 = Label(self.window, text="Usuario")
        self.label2.grid(row =2, column =70)
        self.box1 = Entry(self.window, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box1.grid(row = 2, column =100)
        self.label3 = Label(self.window, text="Contraseña")
        self.label3.grid(row =4, column =70)
        self.box2 = Entry(self.window, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11))
        self.box2.config(show= "*")
        self.box2.grid(row =4,column =100 )
   
        self.button = Button(self.window, text="Continuar", command=self.ButtonEvent)
        self.button.grid(row=6, column = 100)
        self.window.mainloop()


