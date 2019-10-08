from PyQt5.QtWidgets import QDialog
from uis.ui_login_dialog import Ui_Dialog
from core import c_nanoAPI as nanoApi

class Login_dialog(QDialog,Ui_Dialog):
    def __init__(self,*args,**kwargs):
        super(Login_dialog,self).__init__(*args,**kwargs)
        self.setupUi(self)

def my_costum_fn(s):
    print("click",s)

    dlg=Login_dialog()
    if dlg.exec_():
        print("Success!")
        successful, msg= nanoApi.api.sign_in(dlg.get_username(),dlg.get_password())
        if successful:
            print(nanoApi.api.auth)
        else:
            #TODO cases for different errormsg
            print(msg)
    else:
        print("Cancel!")