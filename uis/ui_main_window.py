from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core import login


class Ui_MainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("Main Window")

        # Body des Programmes im Moment nur ein Hallo World label
        #TODO Sinnvollen Body schreiben
        label = QLabel("Hallo World!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)  # erzeugt Widget in der Mitte des Fensters. In diesem Fall das Label

        # erstellt die Toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setObjectName("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))  # groeße der Icons in der Toolbar muss festgelegt werden
        self.addToolBar(toolbar)

        # Login Aktion
        self.login_action = QAction(QIcon("Resources/Symbols/lock-unlock.png"), "Login", self)
        self.login_action.setCheckable(False)
        self.login_action.triggered.connect(login.open_login_dialog)
        self.login_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_L))
        toolbar.addAction(self.login_action)

        # andere Aktion
        #TODO durch sinnvolle Aktionen ersetzten
        self.logout_action = QAction(QIcon("Resources/Symbols/lock.png"), "Logout", self)
        self.logout_action.setCheckable(False)
        self.logout_action.triggered.connect(login.logout)
        toolbar.addAction(self.logout_action)


        # erstellt Statusbar in einer Zeile, auch zweizeilig ware moeglich
        self.setStatusBar(QStatusBar(self))

        # erstellt ein menu
        menu = self.menuBar()

        #Hauptmenu
        main_menu = menu.addMenu("NaNoStatistics")
        main_menu.addAction(self.login_action)
        main_menu.addAction(self.logout_action)
        main_menu.addSeparator()
        #TODO: submenu durch sinnvolles Menu ersetzen oder loeschen
        file_submenu = main_menu.addMenu("Submenu")
        file_submenu.addAction(self.logout_action)

        self.retranslateUi(mainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","NaNo Statistik"))
        self.login_action.setStatusTip(_translate("MainWindow","In Nano Seite einloggen."))
        self.login_action.setText(_translate("MainWindow","Login"))
        self.logout_action.setStatusTip(_translate("MainWindow","In Nano Seite ausloggen."))
        self.logout_action.setText(_translate("MainWindow", "Logout"))