import sys, sqlite3, re, string
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from main_screen import  Ui_MainScreen
from save_word_screen import Ui_SaveWordScreen
from dictionary_screen import  Ui_DictionaryScreen
from firebase import firebase


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
        word = self.ui.tb_word.text()
        meaning = self.ui.tb_meaning.toPlainText()

        test_word = re.sub('[^A-Za-z]+', '', word)
        test_meaning = re.sub('[^A-Za-z]+', '', meaning)
        if test_word != "" and test_meaning != "":
            print(test_word + ", " + test_meaning)
            word.lower()
            meaning.lower()
            meaning_words = meaning.split(",")

            data = {
                "word": word,
                "meaning": meaning_words
            }

            
            fb_con = firebase.FirebaseApplication("https://laside-6b158.firebaseio.com/", None)
            result = fb_con.post("/users/user2", data)
            print(result)      

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