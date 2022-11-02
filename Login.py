class Login():
    def login(self, string, string2, list):
        usernameslist = []
        passwordlist = []
        for i in list["Username"]:
            usernameslist.append(i)
        for i in list["Password"]:
            passwordlist.append(i)

        if string in usernameslist:
            index = usernameslist.index(string)
            if (string == usernameslist[index] and str(string2) == str(passwordlist[index])):
                return True
            else: 
                return False

        else: 
            return False

        
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
    def newTutor(self):
        pass
