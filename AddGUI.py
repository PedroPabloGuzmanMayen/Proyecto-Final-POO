
from tkinter import *
class AddGUI:

    def addMaterial(self):
        pass
    def __init__(self, string, string2, string3, string4, string5):
        self.window = Tk()
        self.window.title(string) 
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.label1 = Label(self.window, text=string, font=("Arial", 50)) 
        self.label1.pack()
        self.frame = Frame(self.window, width=350, height=390)
        self.frame.place(x=300, y =100)
        self.label2 = Label(self.frame, text=string2)
        self.label2.pack()
        self.box1 = Entry(self.frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box1.pack()
        self.label3 = Label(self.frame, text=string3)
        self.label3.pack()
        self.box2 = Entry(self.frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box2.pack()
        self.label3 = Label(self.frame, text=string4)
        self.label3.pack()
        self.box3 = Entry(self.frame, width=25, fg="black", border=2,bg = "white", font =("Comic sans", 11) )
        self.box3.pack()
        self.button = Button(self.frame, text=string5, command=self.addMaterial)
        self.button.pack()
        self.window.mainloop()