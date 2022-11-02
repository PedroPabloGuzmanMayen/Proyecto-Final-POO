from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from Login import Login
from Menu import menu
import pandas as pd

class loginGUI: 

    def Buttonevent(self):
            user0 = self.box1.get()
            pass0 = self.box2.get()
            data = pd.read_excel("users_data.xlsx")
            self.log = Login()

            if self.log.login(user0, pass0,data ):
                self.window.destroy()
                menu()
            else:
                messagebox.showerror(message= "El usuario y la contraseña son incorrectos o el usuario no existe ", title="Mensaje de error")


    def __init__(self):

        self.window = Tk()
        self.window.title("Sign Up")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")

        self.img1 = PhotoImage(file = "duo.png")
        Label(self.window, image= self.img1, border =0, bg = "white").place(x = 50, y=90)

        self.frame = Frame(self.window, width=350, height=390, bg="red")
        self.frame.place(x=480, y =50)
        self.heading = Label(self.frame, text="Ingresa a Knower", fg ="#57a1f8", bg="white", font =("Comic sans", 23, BOLD) )
        self.heading.place(x=85, y=5)
        self.heading2 = Label(self.frame, text="Usuario: ",  fg ="#0a0a0a", bg="white", font =("Comic sans", 11, BOLD))
        self.heading2.place(x=20, y=80)
        self.box1 = Entry(self.frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box1.place(x=100,y=80)
        self.box2 = Entry(self.frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11))
        self.box2.config(show= "*")
        self.box2.place(x=100, y=150)
        self.heading3 = Label(self.frame, text="Contraseña: ",  fg ="#0a0a0a", bg="white", font =("Comic sans", 11, BOLD))
        self.heading3.place(x= 20,y=150)
        self.button1 = Button(self.frame, text ="Comenzar", command= self.Buttonevent)
        self.button1.place(x=120, y=300)
        self.window.mainloop()

