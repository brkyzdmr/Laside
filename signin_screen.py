# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignInScreen(object):
    def setupUi(self, SignInScreen):
        SignInScreen.setObjectName("SignInScreen")
        SignInScreen.resize(340, 400)
        SignInScreen.setMinimumSize(QtCore.QSize(340, 400))
        SignInScreen.setMaximumSize(QtCore.QSize(340, 400))
        font = QtGui.QFont()
        font.setFamily("LMSansQuot8")
        SignInScreen.setFont(font)
        SignInScreen.setStyleSheet("#SignInScreen { background-color: #ffffff; }\n"
"\n"
"QLabel { color: white; }\n"
"QLineEdit { \n"
"border-radius: 10px;\n"
"padding: 0 5px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #27a9e3;\n"
"  border-width: 0px;\n"
"  border-radius: 10px;\n"
"}\n"
"QPushButton:hover { background-color: #66c011; }\n"
"\n"
"#loginForm\n"
"{\n"
"  background: rgb(96, 125, 139);\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(SignInScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.loginForm = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginForm.setFont(font)
        self.loginForm.setStyleSheet("")
        self.loginForm.setObjectName("loginForm")
        self.gridLayout = QtWidgets.QGridLayout(self.loginForm)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_email = QtWidgets.QLabel(self.loginForm)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_email.setFont(font)
        self.lbl_email.setStyleSheet("background-color: rgba( 255, 255, 255, 0% )")
        self.lbl_email.setObjectName("lbl_email")
        self.verticalLayout_2.addWidget(self.lbl_email)
        self.lbl_password = QtWidgets.QLabel(self.loginForm)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_password.setFont(font)
        self.lbl_password.setStyleSheet("background-color: rgba( 255, 255, 255, 0% )")
        self.lbl_password.setObjectName("lbl_password")
        self.verticalLayout_2.addWidget(self.lbl_password)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tb_email = QtWidgets.QLineEdit(self.loginForm)
        self.tb_email.setMinimumSize(QtCore.QSize(200, 25))
        self.tb_email.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tb_email.setFont(font)
        self.tb_email.setToolTip("")
        self.tb_email.setObjectName("tb_email")
        self.verticalLayout.addWidget(self.tb_email)
        self.tb_password = QtWidgets.QLineEdit(self.loginForm)
        self.tb_password.setMinimumSize(QtCore.QSize(200, 25))
        self.tb_password.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tb_password.setFont(font)
        self.tb_password.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tb_password.setObjectName("tb_password")
        self.verticalLayout.addWidget(self.tb_password)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.btn_signin = QtWidgets.QPushButton(self.loginForm)
        self.btn_signin.setMinimumSize(QtCore.QSize(96, 25))
        self.btn_signin.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_signin.setFont(font)
        self.btn_signin.setStyleSheet("")
        self.btn_signin.setObjectName("btn_signin")
        self.verticalLayout_3.addWidget(self.btn_signin)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.btn_signup = QtWidgets.QPushButton(self.loginForm)
        self.btn_signup.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_signup.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("")
        self.btn_signup.setObjectName("btn_signup")
        self.gridLayout.addWidget(self.btn_signup, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.loginForm, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 1)
        SignInScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignInScreen)
        self.btn_signin.clicked.connect(SignInScreen.btn_signin_clicked)
        self.btn_signin.clicked.connect(SignInScreen.btn_signup_clicked)
        QtCore.QMetaObject.connectSlotsByName(SignInScreen)

    def retranslateUi(self, SignInScreen):
        _translate = QtCore.QCoreApplication.translate
        SignInScreen.setWindowTitle(_translate("SignInScreen", "Sign-in"))
        self.lbl_email.setText(_translate("SignInScreen", "E-mail:"))
        self.lbl_password.setText(_translate("SignInScreen", "Password:"))
        self.tb_password.setToolTip(_translate("SignInScreen", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_signin.setText(_translate("SignInScreen", "Sign In"))
        self.btn_signup.setText(_translate("SignInScreen", "Sign Up"))

