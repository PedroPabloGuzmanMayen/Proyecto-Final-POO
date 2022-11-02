from tkinter import *
from PIL import ImageTk, Image
from LoginGUI import loginGUI
from NewAccountGUI import NewAccount
from TutorCreationGUI import createNewTutor
class SelectLogin:

    def changeToLogin(self):
        self.window1.destroy()
        loginGUI()
    def changeToNew(self):
        self.window1.destroy()
        NewAccount()
    def changeToTutorCreation(self):
        self.window1.destroy()
        createNewTutor()

    def __init__(self):
        self.window1 = Tk()
        self.window1.title("Select an option")
        self.window1.geometry("925x500+300+200")
        self.window1.configure(bg = "#fff")
        self.img = Image.open("Logox.png")
        self.resized = self.img.resize((400,300), Image.ANTIALIAS)
        self.newimg = ImageTk.PhotoImage(self.resized)
        Label(self.window1, image = self.newimg, border =0, bg = "white").place(x=50, y = 100)
        self.button1 = Button(self.window1, text = "Iniciar sesión", command=self.changeToLogin)
        self.button1.place(x=600, y=150)
        self.button2 = Button(self.window1, text = "Nueva cuenta", command = self.changeToNew)
        self.button2.place(x =600, y= 250)
        self.label = Label(self.window1, text="Epistemas", font=("Arial, 50"))
        self.label.pack()
        self.button3 = Button(self.window1, text = "Nueva cuenta de tutor", command = self.changeToTutorCreation)
        self.button3.place(x=600, y=350)
        self.window1.mainloop()

hola = SelectLogin()



