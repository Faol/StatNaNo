class Settings(object):
    def __init__(self,saveLogin=False,benutzername=None,pw=None,autoLogin=False):
        self.saveLogin=saveLogin
        self.autoLogin=autoLogin
        self.benutzername=benutzername
        self.password=pw
    def loadSettings(self):
        #TODO write loadSettings funciton
        pass
    def saveSettings(selfs):
        #TODO write saveSettings function
        pass

settings=Settings()