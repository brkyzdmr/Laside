# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_word_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SaveWordScreen(object):
    def setupUi(self, SaveWordScreen):
        SaveWordScreen.setObjectName("SaveWordScreen")
        SaveWordScreen.resize(340, 400)
        SaveWordScreen.setMinimumSize(QtCore.QSize(340, 400))
        SaveWordScreen.setMaximumSize(QtCore.QSize(340, 400))
        font = QtGui.QFont()
        font.setFamily("LMSansQuot8")
        font.setItalic(False)
        SaveWordScreen.setFont(font)
        SaveWordScreen.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(SaveWordScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.lbl_word = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.lbl_word.setFont(font)
        self.lbl_word.setStyleSheet("background-color: rgba( 255, 255, 255, 0% )")
        self.lbl_word.setObjectName("lbl_word")
        self.verticalLayout_2.addWidget(self.lbl_word)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.lbl_meaning = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.lbl_meaning.setFont(font)
        self.lbl_meaning.setStyleSheet("background-color: rgba( 255, 255, 255, 0% )")
        self.lbl_meaning.setObjectName("lbl_meaning")
        self.verticalLayout_2.addWidget(self.lbl_meaning)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tb_word = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.tb_word.setFont(font)
        self.tb_word.setObjectName("tb_word")
        self.verticalLayout.addWidget(self.tb_word)
        self.tb_meaning = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.tb_meaning.setFont(font)
        self.tb_meaning.setObjectName("tb_meaning")
        self.verticalLayout.addWidget(self.tb_meaning)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgba( 255, 255, 255, 0% )")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgb(255, 87, 20)")
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_2.addWidget(self.btn_back)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("background-color: rgb(110, 235, 131)")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        SaveWordScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SaveWordScreen)
        self.btn_back.clicked.connect(SaveWordScreen.btn_back_clicked)
        self.btn_save.clicked.connect(SaveWordScreen.btn_save_clicked)
        QtCore.QMetaObject.connectSlotsByName(SaveWordScreen)

    def retranslateUi(self, SaveWordScreen):
        _translate = QtCore.QCoreApplication.translate
        SaveWordScreen.setWindowTitle(_translate("SaveWordScreen", "Laside - Save Word"))
        self.lbl_word.setText(_translate("SaveWordScreen", "Word:"))
        self.lbl_meaning.setText(_translate("SaveWordScreen", "Meaning:"))
        self.comboBox.setItemText(0, _translate("SaveWordScreen", "New List"))
        self.comboBox.setItemText(1, _translate("SaveWordScreen", "asdad"))
        self.comboBox.setItemText(2, _translate("SaveWordScreen", "asdad"))
        self.btn_back.setText(_translate("SaveWordScreen", "Back"))
        self.btn_save.setText(_translate("SaveWordScreen", "Save"))

