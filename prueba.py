import pandas as pd
from Login import Login
xd = pd.read_excel("users_data.xlsx")
def determine(a):
    a = 3
    if a ==4:
        return True
    else:
        return False

hola = 4

print(xd.loc[0]["Username"])

if (determine(hola)):
    print("adios")

print(xd[xd["Username"].str.match("holi")])

print("adios" in xd["Username"].unique())

home = Login()

prueba = input("Ingresa el nombre")
prueba2 = input("Ingresa la contraseña")

if (home.login(prueba, prueba2, xd)):
    print("wa")


lista = []

for i in xd["Username"]:
    lista.append(i)

print(lista)

print(prueba in lista)