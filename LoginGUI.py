from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import Login
import Login
class loginGUI: 

    def __init__(self):

        window = Tk()
        window.title("Sign Up")
        window.geometry("925x500+300+200")
        window.configure(bg = "#fff")

        img = PhotoImage(file = "duo.png")
        Label(window, image = img, border =0, bg = "white").place(x = 50, y=90)

        frame = Frame(window, width=350, height=390, bg="red")
        frame.place(x=480, y =50)
        heading = Label(frame, text="Ingresa a Knower", fg ="#57a1f8", bg="white", font =("Comic sans", 23, BOLD) )
        heading.place(x=85, y=5)
        heading2 = Label(frame, text="Usuario: ",  fg ="#0a0a0a", bg="white", font =("Comic sans", 11, BOLD))
        heading2.place(x=20, y=80)
        box1 = Entry(frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        box1.place(x=100,y=80)
        box2 = Entry(frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11))
        box2.place(x=100, y=150)
        heading3 = Label(frame, text="Contraseña: ",  fg ="#0a0a0a", bg="white", font =("Comic sans", 11, BOLD))
        heading3.place(x= 20,y=150)
        button1 = Button(frame, text ="Comenzar")
        button1.place(x=120, y=300)
        window.mainloop()

hola = loginGUI()
