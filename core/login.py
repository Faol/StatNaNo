from PyQt5.QtWidgets import QDialog

from core.c_settings import settings
from uis import ui_login_dialog
from uis.ui_login_dialog import Ui_Dialog
from core import c_nanoAPI as nanoApi

class Login_dialog(QDialog,Ui_Dialog):
    def __init__(self,*args,**kwargs):
        super(Login_dialog,self).__init__(*args,**kwargs)
        self.setupUi(self)

def open_login_dialog(s):
    dlg=Login_dialog()
    if dlg.exec_():
        successful, msg, errorCode = nanoApi.api.sign_in(dlg.get_username(),dlg.get_password())
        settings.saveLogin=dlg.getSaveLoginState()
        if dlg.getSaveLoginState():
            settings.benutzername=dlg.get_username()
            settings.password=dlg.get_password()
        else:
            settings.benutzername =None
            settings.password =None
        settings.autoLogin=dlg.getAutoLoginState()
        if successful:
            print(nanoApi.api.auth)
        else:
            if errorCode==1:
                ui_login_dialog.loginErrorMessageRetry(msg)
            else:
                ui_login_dialog.loginErrorMessage(msg)
    else:
        pass

def retry_login_dialog():
    open_login_dialog(True)

def logout(s):
    nanoApi.api.logout()
    print(nanoApi.api.auth)