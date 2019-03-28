import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from main_screen import  Ui_MainScreen
from save_word_screen import Ui_SaveWordScreen
from dictionary_screen import  Ui_DictionaryScreen
class MainScreen(QMainWindow):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent=parent)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)
        self.show()
    def btn_saveword_clicked(self):
        window = SaveWordScreen(self)
        window.show()
        self.hide()
    def btn_dictionary_clicked(self):
        print(" Clicked!")
        window = DictionaryScreen(self)
        window.show()
        self.hide()
    def btn_settings_clicked(self):
        print("Settings clicked!")

class SaveWordScreen(QMainWindow):
    def __init__(self, parent=None):
        super(SaveWordScreen, self).__init__(parent=parent)
        self.ui = Ui_SaveWordScreen()
        self.ui.setupUi(self)
    def btn_back_clicked(self):
        window = MainScreen(self)
        window.show()
        self.hide()
    def btn_save_clicked(self):
        print("Save clicked!")

class DictionaryScreen(QMainWindow):
    def __init__(self, parent=None):
        super(DictionaryScreen, self).__init__(parent=parent)
        self.ui = Ui_DictionaryScreen()
        self.ui.setupUi(self)
    def btn_back_clicked(self):
        window = MainScreen(self)
        window.show()
        self.hide()

def main():
    app = QApplication(sys.argv)
    window = MainScreen()


    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()