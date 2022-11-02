from tkinter import *
from LoginGUI import user
class SelectLogin:

    def __init__(self):
        self.window1 = Tk()
        self.window1.title("Select an option")
        self.window1.geometry("925x500+300+200")
        self.window1.configure(bg = "#fff")
        self.img = PhotoImage(file = "Logox.png")
        Label(self.window1, image = self.img, border =0, bg = "white").pack()
        button1 = Button(self.window1)
        self.window1.mainloop()

print(user)

