class AddData:
    def newAccount(self, string, string2, boolean, score, db):
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
    def newTutor(self, string, string2, string3, db):
        list1 = [str(string), str(string2), str(string3)]
        db.loc[len(db)] = list1
        db.to_excel("Tutors.xlsx", index = False)