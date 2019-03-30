# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsScreen(object):
    def setupUi(self, SettingsScreen):
        SettingsScreen.setObjectName("SettingsScreen")
        SettingsScreen.resize(340, 400)
        SettingsScreen.setMinimumSize(QtCore.QSize(340, 400))
        SettingsScreen.setMaximumSize(QtCore.QSize(340, 400))
        font = QtGui.QFont()
        font.setFamily("LMSansQuot8")
        font.setItalic(True)
        SettingsScreen.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SettingsScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_signup = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("background-color: rgb(166, 130, 255)")
        self.btn_signup.setObjectName("btn_signup")
        self.horizontalLayout.addWidget(self.btn_signup)
        self.btn_signin = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.btn_signin.setFont(font)
        self.btn_signin.setStyleSheet("background-color: rgb(88, 135, 255)")
        self.btn_signin.setObjectName("btn_signin")
        self.horizontalLayout.addWidget(self.btn_signin)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgb(255, 87, 20)")
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 2, 0, 1, 1)
        SettingsScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsScreen)
        self.btn_signin.clicked.connect(SettingsScreen.btn_signin_clicked)
        self.btn_signup.clicked.connect(SettingsScreen.btn_signup_clicked)
        self.btn_back.clicked.connect(SettingsScreen.btn_back_clicked)
        QtCore.QMetaObject.connectSlotsByName(SettingsScreen)

    def retranslateUi(self, SettingsScreen):
        _translate = QtCore.QCoreApplication.translate
        SettingsScreen.setWindowTitle(_translate("SettingsScreen", "Laside - Settings"))
        self.btn_signup.setText(_translate("SettingsScreen", "Sign-up"))
        self.btn_signin.setText(_translate("SettingsScreen", "Sign-in"))
        self.btn_back.setText(_translate("SettingsScreen", "Back"))

