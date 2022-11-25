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

    def getQuestions(self, score):
        globalquestions = pd.read_excel("Questions.xlsx")
        if (score <= 500):
            questions = globalquestions[globalquestions.Level == 1]
        if ( 500 < score <= 1000):
            questions = globalquestions[globalquestions.Level == 2]
        if (1000 < score <= 1500):
            questions = globalquestions[globalquestions.Level == 3]
        if (1500 < score ):
            questions = globalquestions[globalquestions.Level == 4]

        return questions