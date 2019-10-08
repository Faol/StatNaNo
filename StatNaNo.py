#import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


from core import exceptions, c_nanoAPI as nanoApi
from core.c_person import PersonManager
from uis.ui_main_window import Ui_MainWindow

#--------------------------------
# bei Programmstart
#--------------------------------
personenManager=PersonManager(nanoApi.api)


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        self.setupUi(self)
        #gibt dem Fenster einen Titel




#enthaelt die Eventschleife, nur eine pro Programm
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# startete die Eventschleife
app.exec_()

#--------------------------------
# test code
#--------------------------------


#personenManager.addNew("Faol","faol")
#personenManager.addNew("Janika","winged_charly")
#personenManager.addNew("Kraehe","kraehe")

#nanoApi.api.fileFromAPI("https://api.nanowrimo.org/project-challenges/1937667/project-sessions","project_sessions_Bienenkinder")
#nanoApi.api.fileFromAPI("https://api.nanowrimo.org/project-challenges/1547715/project-sessions","project_kraehe")


#print(personenManager.persons)
#print(vars(personenManager.persons["669340"]))

print("Done")