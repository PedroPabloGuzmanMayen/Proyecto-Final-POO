from tkinter import *
from AddData import AddData
import pandas as pd
from AddGUI import AddGUI
class AddTutor(AddGUI):

    def addMaterial(self):
        self.add = AddData()
        self.add.newTutor(self.box1.get(), self.box3.get(), self.box2.get())
        self.box1.delete(0, END)
        self.box2.delete(0, END)
        self.box3.delete(0, END)


     
