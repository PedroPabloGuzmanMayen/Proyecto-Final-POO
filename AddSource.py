from tkinter import *
from AddData import AddData
from AddGUI import AddGUI
class AddSourceGUI(AddGUI):

    def addMaterial(self):
        self.add = AddData()
        self.add.newSource(self.box1.get(), self.box3.get(), self.box2.get())
        self.box1.delete(0, END)
        self.box2.delete(0, END)
        self.box3.delete(0, END)
    
