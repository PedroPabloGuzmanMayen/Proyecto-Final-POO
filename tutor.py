from user import user
class tutor(user): 
    def getrealname(self):
        return self.realname
    def setrealname(self, realname):
        self.realname = realname
    def getphone(self):
        return self.phone
    def setphone(self, phone):
        self.phone = phone
    def getemail(self):
        return self.email
    def setemail(self, email):
        self.email = email
