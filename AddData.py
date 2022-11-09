import pandas as pd
class AddData:
    def newAccount(self, string, string2, boolean, score):
        db = pd.read_excel("users_data.xlsx")
        usernameslist = []
        for i in db["Username"]:
            usernameslist.append(i)
        if (string in usernameslist):
            return False
        else:
            list1 = [str(string), str(string2), bool(boolean), int(score)]
            db.loc[len(db)] = list1
            db.to_excel("users_data.xlsx", index = False)
            return True
    def newTutor(self, string, string2, string3):
        db = pd.read_excel("Tutors.xlsx")
        list1 = [str(string), str(string2), str(string3)]
        db.loc[len(db)] = list1
        db.to_excel("Tutors.xlsx", index = False)

    def newSource(self, string, string2, level):
        db = pd.read_excel("Resources.xlsx")
        list1 = [str(string), str(string2), int(level)]
        db.loc[len(db)] = list1
        db.to_excel("Resources.xlsx", index = False)