# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dictionary_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DictionaryScreen(object):
    def setupUi(self, DictionaryScreen):
        DictionaryScreen.setObjectName("DictionaryScreen")
        DictionaryScreen.resize(340, 400)
        DictionaryScreen.setMinimumSize(QtCore.QSize(340, 400))
        DictionaryScreen.setMaximumSize(QtCore.QSize(340, 400))
        font = QtGui.QFont()
        font.setFamily("LMSansQuot8")
        font.setItalic(True)
        DictionaryScreen.setFont(font)
        DictionaryScreen.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(DictionaryScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tw_wordtable = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.tw_wordtable.setFont(font)
        self.tw_wordtable.setFrameShape(QtWidgets.QFrame.Box)
        self.tw_wordtable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tw_wordtable.setGridStyle(QtCore.Qt.SolidLine)
        self.tw_wordtable.setWordWrap(False)
        self.tw_wordtable.setObjectName("tw_wordtable")
        self.tw_wordtable.setColumnCount(2)
        self.tw_wordtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LMSansQuot8")
        font.setItalic(True)
        item.setFont(font)
        self.tw_wordtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LMSansQuot8")
        font.setItalic(True)
        item.setFont(font)
        self.tw_wordtable.setHorizontalHeaderItem(1, item)
        self.tw_wordtable.horizontalHeader().setHighlightSections(True)
        self.tw_wordtable.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tw_wordtable)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setItalic(False)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgb(255, 87, 20)")
        self.btn_back.setObjectName("btn_back")
        self.verticalLayout.addWidget(self.btn_back)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        DictionaryScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(DictionaryScreen)
        self.btn_back.clicked.connect(DictionaryScreen.btn_back_clicked)
        QtCore.QMetaObject.connectSlotsByName(DictionaryScreen)

    def retranslateUi(self, DictionaryScreen):
        _translate = QtCore.QCoreApplication.translate
        DictionaryScreen.setWindowTitle(_translate("DictionaryScreen", "Laside - Dictionary"))
        item = self.tw_wordtable.horizontalHeaderItem(0)
        item.setText(_translate("DictionaryScreen", "Word"))
        item = self.tw_wordtable.horizontalHeaderItem(1)
        item.setText(_translate("DictionaryScreen", "Meaning"))
        self.btn_back.setText(_translate("DictionaryScreen", "Back"))

