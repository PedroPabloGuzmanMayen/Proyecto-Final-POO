from tkinter import*
import matplotlib.pyplot as plt
import pandas as pd
class compareScore:

    def showgraph(self):
        db = pd.read_excel("users_data.xlsx", index_col = 0)
        db = db[["Score"]]
        db.plot(kind = "barh", xlabel = "Usuarios", ylabel = "Usuarios", title = "Puntaje de los usuarios", stacked = True, colormap = "Accent")
        plt.show()

    def __init__(self):
        self.window = Tk()
        self.window.title("Comparar el puntaje")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg = "#fff")
        self.compareButton = Button(self.window, text = "Compara tu puntaje!", font=("Arial", 50), command=self.showgraph)
        self.compareButton.pack()
        self.window.mainloop()
