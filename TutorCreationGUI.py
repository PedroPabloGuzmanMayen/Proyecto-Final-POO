from tkinter import * 
class createNewTutor:
     def __init__(self):
        self.window = Tk()
        self.window.title("Crea tu cuenta")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.label = Label(self.window, text="Crea tu cuenta de tutor", font=("Arial, 50"))
        self.label.grid(row =0, column=80)
        self.label2 = Label(self.window, text="Usuario")
        self.label2.grid(row =10, column =70)
        self.box1 = Entry(self.window, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box1.grid(row = 10, column =100)
        self.label3 = Label(self.window, text="Contraseña")
        self.label3.grid(row =20, column =70)
        self.box2 = Entry(self.window, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11))
        self.box2.config(show= "*")
        self.box2.grid(row =20,column =100 )
   
        self.label5 =Label(self.window,text="Numero de telefono" )
        self.label5.grid(row = 30, column = 70)
        self.box3 = Entry(self.window, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11))
        self.box3.grid(row=30, column=100)
        self.label6 =Label(self.window,text="Nombre real" )
        self.label6.grid(row = 40, column = 70)
        self.box4 = Entry(self.window, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11))
        self.box4.grid(row=40, column=100)
        self.label7 =Label(self.window,text="Correo electrónico" )
        self.label7.grid(row = 50, column = 70)
        self.box4 = Entry(self.window, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11))
        self.box4.grid(row=50, column=100)
    

        self.window.mainloop()

