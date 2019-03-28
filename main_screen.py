# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(200, 400)
        MainScreen.setMinimumSize(QtCore.QSize(200, 400))
        MainScreen.setMaximumSize(QtCore.QSize(200, 400))
        font = QtGui.QFont()
        font.setFamily("LMSansQuot8")
        MainScreen.setFont(font)
        MainScreen.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_saveword = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_saveword.sizePolicy().hasHeightForWidth())
        self.btn_saveword.setSizePolicy(sizePolicy)
        self.btn_saveword.setStyleSheet("background-color: rgb(236, 236, 236)")
        self.btn_saveword.setObjectName("btn_saveword")
        self.verticalLayout.addWidget(self.btn_saveword)
        self.btn_lookup = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_lookup.sizePolicy().hasHeightForWidth())
        self.btn_lookup.setSizePolicy(sizePolicy)
        self.btn_lookup.setStyleSheet("background-color: rgb(236, 236, 236)")
        self.btn_lookup.setObjectName("btn_lookup")
        self.verticalLayout.addWidget(self.btn_lookup)
        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setStyleSheet("background-color: rgb(236, 236, 236)")
        self.btn_settings.setObjectName("btn_settings")
        self.verticalLayout.addWidget(self.btn_settings)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainScreen)
        self.btn_saveword.clicked.connect(MainScreen.btn_saveword_clicked)
        self.btn_lookup.clicked.connect(MainScreen.btn_lookup_clicked)
        self.btn_settings.clicked.connect(MainScreen.btn_settings_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "Laside"))
        self.btn_saveword.setText(_translate("MainScreen", "Save Word"))
        self.btn_lookup.setText(_translate("MainScreen", "Look Up"))
        self.btn_settings.setText(_translate("MainScreen", "Settings"))

