from tkinter import *
class SelectLogin:

    def __init__(self):
        window1 = Tk()
        window1.title("Select an option")
        window1.geometry("925x500+300+200")
        window1.configure(bg = "#fff")
        img = PhotoImage(file = "Logo (1).png")
        Label(window1, image = img, border =0, bg = "white").place(x = 50, y=90)

adios = SelectLogin()
