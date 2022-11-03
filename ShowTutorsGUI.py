from tkinter import*
from tkinter import ttk
import pandas as pd
import numpy as np
class ShowTutors:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mostrar los recursos educativos")
        self.window.geometry("925x500+300+200")
        self.mydata = pd.read_excel("Tutors.xlsx")
        self.frame = Frame(self.window)
        self.frame.pack(pady =20)
        self.tree = ttk.Treeview(self.frame)
        self.tree["column"] = list(self.mydata.columns)
        self.tree["show"] = "headings"
        for col in self.tree["column"]:
            self.tree.heading(col, text=col)
        self.row = self.mydata.to_numpy().tolist()
        for rows in self.row:
            self.tree.insert("", "end", values=rows)

        self.tree.pack()
        self.window.mainloop()