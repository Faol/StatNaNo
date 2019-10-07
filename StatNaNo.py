#import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from uis.ui_login_dialog import Ui_Dialog
from core import exceptions, c_nanoAPI as nanoApi
from core.c_person import PersonManager

#--------------------------------
# bei Programmstart
#--------------------------------

personenManager=PersonManager(nanoApi.api)
#--------------------------------
# test code
#--------------------------------



class Login_dialog(QDialog,Ui_Dialog):
    def __init__(self,*args,**kwargs):
        super(Login_dialog,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.setWindowTitle("Login")

class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        #gibt dem Fenster einen Titel
        self.setWindowTitle("Meine erste App!")
        #erstellt ein Label
        label=QLabel("Hallo World!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label) #erzeugt Widget in der Mitte des Fensters. In diesem Fall das Label
        #erstellt eine Toolbar
        toolbar= QToolBar("Meine erste Toolbar")
        toolbar.setIconSize(QSize(16,16)) #groeße der Icons in der Toolbar muss festgelegt werden
        self.addToolBar(toolbar)
        #Aktionen ermoeglichen das mehrere Eingaben die gleiche Aktion hervor rufen
        my_button_action =QAction(QIcon("Resources/Symbols/lock-unlock.png"),"Mein erster Button",self)
        my_button_action.setStatusTip("Das ist mein toller Button")
        my_button_action.setCheckable(True)
        my_button_action.triggered.connect(self.my_costum_fn)
        my_button_action.setShortcut(QKeySequence(Qt.CTRL+Qt.SHIFT+Qt.Key_S))
        toolbar.addAction(my_button_action)

        #andere Aktion
        my_button_action2 =QAction(QIcon("disk--plus.png"),"Mein zweiter Button",self)
        my_button_action2.setStatusTip("Das ist mein bloeder Button")
        my_button_action2.setCheckable(True)
        my_button_action2.triggered.connect(self.my_costum_fn)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        #erstellt Statusbar in einer Zeile, auch zweizeilig ware moeglich
        self.setStatusBar(QStatusBar(self))
        #erstellt ein menu
        menu=self.menuBar()
        #menu.setNativeMenuBar(False)
        file_menu=menu.addMenu("&File")
        file_menu.addAction(my_button_action)
        file_menu.addSeparator()

        file_submenu=file_menu.addMenu("Submenu")
        file_submenu.addAction(my_button_action2)

    def my_costum_fn(self,s):
        print("click",s)

        dlg=Login_dialog(self)
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
#enthaelt die Eventschleife, nur eine pro Programm
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# startete die Eventschleife
app.exec_()

    
#personenManager.addNew("Faol","faol")
#personenManager.addNew("Janika","winged_charly")
#personenManager.addNew("Kraehe","kraehe")

#nanoApi.api.fileFromAPI("https://api.nanowrimo.org/project-challenges/1937667/project-sessions","project_sessions_Bienenkinder")
#nanoApi.api.fileFromAPI("https://api.nanowrimo.org/project-challenges/1547715/project-sessions","project_kraehe")


#print(personenManager.persons)
#print(vars(personenManager.persons["669340"]))

print("Done")