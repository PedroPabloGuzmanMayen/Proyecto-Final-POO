


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

        
    def newAccount(self):
        pass
