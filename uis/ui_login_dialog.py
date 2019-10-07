# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QDialogButtonBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Login-Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(366, 233)
        Dialog.setAutoFillBackground(False)
        Dialog.setModal(True)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("username")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("password")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("saveLogin")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setObjectName("autoLogin")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Login-Dialog", "NaNo-Login"))
        self.label.setText(_translate("Login-Dialog", "Gibt hier deine NaNo-Login-Daten an."))
        self.lineEdit.setPlaceholderText(_translate("Login-Dialog", "NaNo-Benutzername"))
        self.lineEdit_2.setPlaceholderText(_translate("Login-Dialog", "NaNo-Password", "Password"))
        self.checkBox.setText(_translate("Login-Dialog", "Login Daten speichern"))
        self.checkBox_2.setText(_translate("Login-Dialog", "Beim nächsten öffnen einloggen"))
        self.buttonBox.button(QDialogButtonBox.Ok).setText(_translate("Login-Dialog", "Login"))
    def get_username(self):
        return self.findChild(QLineEdit, "username").text()
    def get_password(self):
        return self.findChild(QLineEdit, "password").text()
